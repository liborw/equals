from dataclasses import dataclass, field
from typing import Iterator


@dataclass
class EqualsLine(object):

    line_num: int
    line_text: str
    col_start: int
    col_end: int
    expression: str
    value: list[str] = field(init=False, default_factory=list)

    def get_updated_lines(self) -> list[str]:

        line_out = self.line_text[:self.col_start]
        line_out += " " + self.value[0]

        if self.col_end > 0:
            line_out += " " + self.line_text[self.col_end:]

        return [line_out]


def process_script_output(lines_in: list[str]) -> Iterator[tuple[int,list[str]]]:

    line_num = None
    value = []

    for line in lines_in:

        if line.startswith('_equals_end'):
            yield line_num, value
            line_num = None
            value = []

        elif line_num is not None:
            value.append(line)

        elif line.startswith('_equals_start:'):
            line_num = int(line.split(':')[1])
