"""Equals (#=): evaluate and update script

Usage:
    equals [options] <input>

Options:
    -i, --in-place
    -d, --debug
    -o PATH, --output PATH
    -u, --updates-only
    -l LANG, --language LANG

"""

import sys
import logging
import fileinput
import json
import docopt
from equals.languages import langmap
from equals.utils import process_script_output

APP_NAME = 'equals'

log = logging.getLogger(APP_NAME)


def main():

    # Process comman line arguments
    args = docopt.docopt(__doc__)

    in_place = args['--in-place']
    debug = args['--debug']
    output = args['--output']
    updates_only = args['--updates-only']
    language = args['--language']
    filepath = args['<input>']


    # setup logging
    logging.basicConfig(level='DEBUG' if debug else 'INFO')

    # get language
    lang = langmap[language]

    # if editing in place output is same as input
    if in_place and not filepath == '-':
        output = filepath

    # read file into list of lines, without linebreaks
    f = fileinput.input(files=(filepath, ))
    lines_in = []
    for line in f:
        lines_in.append(line[:-1])
    f.close()

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
        updates = []
        for el in lines_eq.values():
            updates.append(el.as_dict())
        print(json.dumps(updates))
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


