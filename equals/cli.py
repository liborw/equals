#!/usr/bin/env python

import subprocess
import sys
import logging
import click
import fileinput

EQUALS_TAG = '#='
COMMENT = '#'
APP_NAME = 'equals'

log = logging.getLogger(APP_NAME)


@click.command()
@click.argument('input', type=click.Path(allow_dash=True), default='-')
@click.option('-i', '--in-place', is_flag=True)
@click.option('-d', '--debug', is_flag=True)
@click.option('-o', '--output', type=click.Path(), required=False)
@click.option('-u', '--updates-only', is_flag=True, help="Print just updates to the file")
def cli(input, in_place, debug, output, updates_only):

    # setup logging
    logging.basicConfig(level='DEBUG' if debug else 'INFO')

    # if editing in place output is same as input
    if in_place and not input == '-':
        output = input

    # read file into list of lines, without linebreaks
    with fileinput.input(files=(input)) as f:
        lines_in = []
        for line in f:
            lines_in.append(line[:-1])

    # preprocessing
    lines_pp = preprocess_python(lines_in)

    # execute the modified code
    text = '\n'.join(lines_pp)
    stdout, stderr = execute_python(text)

    # print error and exit if there is one
    if stderr:
        print("There was an error in the input:", file=sys.stderr)
        print(stderr, file=sys.stderr)
        sys.exit(1)

    # post processing
    updates = postprocess_python(stdout.split('\n'))

    # print updates if required
    if updates_only:
        for update in updates:
            print(update)
        sys.exit(0)

    # appli updates
    lines_out = apply_updates(lines_in, updates)

    # output
    text = '\n'.join(lines_out)
    if output:
        with open(output, 'w') as f:
            f.write(text)
    else:
        print(text, end='')


def execute_python(text: str):

    process = subprocess.Popen(
        ['python'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = process.communicate(input=text.encode())

    return stdout.decode(), stderr.decode()


def gen_print_line(expr: str, line: int, start: int, end: int = -1) -> str:

    if '=' in expr:
        parts = expr.split('=')
        expr = parts[1].strip()

    fmt_str = '_equals: {},{},{},{}'
    line_out = f"print('{fmt_str}'.format({line}, {start}, {end}, {expr}))"
    return line_out


def parse_print_output(s: str):

    s = s[len('_equals:'):].strip()
    p1, p2, p3, *rest = s.split(',')

    # parse int
    line, start, end = int(p1), int(p2), int(p3)

    # hacky solusion for , in a value
    value = ','.join(rest)

    return line, start, end, value


def preprocess_python(lines_in: list[str]):
    lines_out = []

    for i, line in enumerate(lines_in):
        lines_out.append(line)
        if EQUALS_TAG in line:
            start = line.index(EQUALS_TAG)
            expr = line[:start].strip()
            start = start + len(EQUALS_TAG)
            try:
                end = start + line[start:].index('#')
            except ValueError:
                end = -1
            line = gen_print_line(expr, i, start, end)
            lines_out.append(line)
    return lines_out


def postprocess_python(lines_in: list[str]):
    updates = []
    for line in lines_in:
        if line.startswith('_equals:'):
            updates.append(parse_print_output(line))
    return updates


def apply_updates(lines: list[str], updates: list):
    for update in updates:
        i, s, e, v = update
        line = lines[i]
        if e >= 0:
            lines[i] = line[:s] + " " + v + " " + line[e:]
        else:
            lines[i] = line[:s] + " " + v
    return lines
