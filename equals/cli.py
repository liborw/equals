#!/usr/bin/env python

import sys
import logging
import click
import fileinput
from equals.languages import langmap
from equals.utils import process_script_output

APP_NAME = 'equals'

log = logging.getLogger(APP_NAME)


@click.command()
@click.argument('input', type=click.Path(allow_dash=True), default='-')
@click.option('-i', '--in-place', is_flag=True)
@click.option('-d', '--debug', is_flag=True)
@click.option('-o', '--output', type=click.Path(), required=False)
@click.option('-u', '--updates-only', is_flag=True, help="Print just updates to the file")
@click.option('-l', '--language', default="python", type=click.Choice(list(langmap.keys())))
def cli(input, in_place, debug, output, updates_only, language):

    # setup logging
    logging.basicConfig(level='DEBUG' if debug else 'INFO')

    # get language
    lang = langmap[language]

    # if editing in place output is same as input
    if in_place and not input == '-':
        output = input

    # read file into list of lines, without linebreaks
    with fileinput.input(files=(input)) as f:
        lines_in = []
        for line in f:
            lines_in.append(line[:-1])

    # preprocessing
    lines_pp, lines_eq = lang.preprocess(lines_in)

    # execute the modified code
    text = '\n'.join(lines_pp)
    stdout, stderr = lang.execute(text)

    # print error and exit if there is one
    if stderr:
        print("There was an error in the input:", file=sys.stderr)
        print(stderr, file=sys.stderr)
        sys.exit(1)

    # post processing
    for i, value in process_script_output(stdout.split('\n')):
        lines_eq[i].value = value

    # print updates if required
    if updates_only:
        for el in lines_eq.values():
            print(el.as_dict())
        sys.exit(0)

    # appli updates
    lines_out = []
    for i, line in enumerate(lines_in):
        if i in lines_eq:
            lines_out.extend(lines_eq[i].get_updated_lines())
        else:
            lines_out.append(line)

    # output
    text = '\n'.join(lines_out)
    if output:
        with open(output, 'w') as f:
            f.write(text)
    else:
        print(text, end='')


