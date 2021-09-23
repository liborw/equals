import subprocess
EQUALS_TAG = '#='


def execute(text: str):

    process = subprocess.Popen(
        ['python'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = process.communicate(input=text.encode())

    return stdout.decode(), stderr.decode()


def preprocess(lines_in: list[str]):
    lines_out = []

    for i, line in enumerate(lines_in):
        lines_out.append(line)
        if EQUALS_TAG in line:
            line_print = _process_equals_line(line, i)
            lines_out.append(line_print)
    return lines_out


def postprocess(lines_in: list[str]):
    updates = []
    for line in lines_in:
        if line.startswith('_equals:'):
            updates.append(_parse_print_output(line))
    return updates


def _split_equals_line(line):
    start = line.index(EQUALS_TAG)
    expr = line[:start].strip()
    start = start + len(EQUALS_TAG)
    try:
        end = start + line[start:].index('#')
    except ValueError:
        end = -1

    return start, end, expr


def _gen_print_line(expr: str, line: int, start: int, end: int = -1) -> str:

    if '=' in expr:
        parts = expr.split('=')
        expr = parts[1].strip()

    fmt_str = '_equals: {},{},{},{}'
    line_out = f"print('{fmt_str}'.format({line}, {start}, {end}, {expr}))"
    return line_out


def _parse_print_output(s: str):

    s = s[len('_equals:'):].strip()
    p1, p2, p3, *rest = s.split(',')

    # parse int
    line, start, end = int(p1), int(p2), int(p3)

    # hacky solusion for , in a value
    value = ','.join(rest)

    return line, start, end, value
