from ..utils import EqualsLine
from .python import _is_equals_line, _process_equals_line, _gen_print_lines
from .python import execute


def preprocess(lines_in: list[str]) -> tuple[list[str], dict[int, EqualsLine]]:
    lines_out = []
    equals_lines = dict()
    in_code_block = False

    for i, line in enumerate(lines_in):
        if in_code_block:
            if line == '```':
                in_code_block = False
            else:
                lines_out.append(line)

                if _is_equals_line(line):
                    start, end, expr = _process_equals_line(line)

                    el = EqualsLine(
                            line_num=i,
                            line_text=line,
                            col_start=start,
                            col_end=end,
                            expression=expr
                    )

                    equals_lines[el.line_num] = el
                    line_print = _gen_print_lines(el)
                    lines_out.extend(line_print)

        if line.startswith('```python'):
            in_code_block = True

    return lines_out, equals_lines







