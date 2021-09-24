import subprocess
from equals.utils import EqualsLine

EQUALS_TAG = '#='


def execute(text: str) -> tuple[str, str]:

    process = subprocess.Popen(
        ['python'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = process.communicate(input=text.encode())
    return stdout.decode(), stderr.decode()


def preprocess(lines_in: list[str]) -> tuple[list[str], dict[int, EqualsLine]]:
    lines_out = []
    equals_lines = dict()

    for i, line in enumerate(lines_in):
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

    return lines_out, equals_lines


def _is_equals_line(line: str) -> bool:
    return EQUALS_TAG in line


def _process_equals_line(line: str) -> tuple[int, int, str]:

    start = line.index(EQUALS_TAG)
    expr = line[:start].strip()
    start = start + len(EQUALS_TAG)

    # fix expression if it is assignment
    if '=' in expr:
        parts = expr.split('=')
        expr = parts[0].strip()

    # fix print function
    if expr.startswith('print('):
        expr = expr[6:-1]

    # find end of the space
    try:
        end = start + line[start:].index('#')
    except ValueError:
        end = -1

    return start, end, expr


def _gen_print_lines(el: EqualsLine) -> list[str]:

    lines_out = [
        f"print('_equals_start:{el.line_num}')",
        f"print({el.expression})",
        f"print('_equals_end:{el.line_num}')",
    ]

    return lines_out
