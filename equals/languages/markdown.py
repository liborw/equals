import re
from .python import

input_file = 'test/test.md'


with open(input_file, 'r') as f:
    content = f.read()
    lines_in = content.split('\n')

def preporcess(lines_in:list[list]):
    lines_out = []
    in_code_block = False

    for _, line in lines_in:



        if in_code_block:
            if line == '```':
                in_code_block = False
            else:
                lines_out.append(line)

        if line.startswith('```python'):
            in_code_block = True








