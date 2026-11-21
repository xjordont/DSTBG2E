"""WeasyPrint column-balancing patch (tested on WeasyPrint 70).

When balancing the last column set of a multi-column container, WeasyPrint grows the trial height by the
height of the first leftover block. Where sections are wrapped in block containers that is a whole section,
so the last page of a chapter ends with one column far longer than the other. This patch makes the step the
height of the first line or first unbreakable block instead. Import this module before rendering."""
import inspect
import weasyprint.layout.block as wblock
import weasyprint.layout.column as wcol
from weasyprint.formatting_structure import boxes  # noqa: F401 (used by the injected helper)

OLD = """                        for child in next_box.children:
                            if child.is_in_normal_flow():
                                next_box_height = child.margin_height()
                                break"""
NEW = """                        next_box_height = _first_unit_height(next_box)"""
HELPER = '''

def _first_unit_height(box):
    """Distance from the top of box to the foot of its first line or first unbreakable block."""
    top = box.content_box_y()
    node = box
    while True:
        first = next((c for c in getattr(node, 'children', []) if c.is_in_normal_flow()), None)
        if first is None:
            return node.margin_height() + node.position_y - top if node is not box else 0
        breakable = (isinstance(first, boxes.BlockBox) and first.children
                     and first.style['break_inside'] not in ('avoid', 'avoid-page', 'avoid-column'))
        if isinstance(first, boxes.LineBox) or not breakable:
            return first.position_y + first.margin_height() - top
        node = first
'''
PATCH_APPLIED = False
if 'PATCHED' not in wcol.__dict__:
    src = inspect.getsource(wcol)
    step = "                add_height = 1 if lost_space == inf else lost_space"
    start = "                        balancing = True\n"
    if OLD in src and step in src and start in src:
        src = src.replace(OLD, NEW) + HELPER
        src = src.replace(step, "                add_height = 1 if lost_space == inf else min(lost_space, 12)")
        src = src.replace(start, start + "                        lost_space = inf\n")
        src = src.replace('from .absolute import absolute_layout',
                          'from .absolute import absolute_layout\nfrom ..formatting_structure import boxes')
        exec(compile(src, wcol.__file__, 'exec'), wcol.__dict__)
        wblock.columns_layout = wcol.columns_layout
        wcol.PATCHED = True
        PATCH_APPLIED = True
    else:  # WeasyPrint changed: render unpatched and say so, rather than fail the build
        print('wp_patch: WeasyPrint source differs from the tested version; column-balancing patch NOT applied')
else:
    PATCH_APPLIED = True
