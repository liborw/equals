import unittest
from equals.languages import python
from equals.utils import EqualsLine


class TestPythonModule(unittest.TestCase):

    def test_process_equals_line(self):
        start, end, expr = python._process_equals_line('1 + 1 #= ')
        assert (start, end, expr) == (8, -1, '1 + 1')

    def test_process_equals_line_assignemnt(self):
        start, end, expr = python._process_equals_line('a = 1 + 1 #= ')
        assert (start, end, expr) == (12, -1, 'a')

    def test_process_equals_line_print(self):
        start, end, expr = python._process_equals_line('print("test") #= ')
        assert (start, end, expr) == (16, -1, '"test"')

    def test_gen_print_lines(self):

        el = EqualsLine(
            line_num=0,
            line_text='1 + 1 #=',
            col_start=6,
            col_end=-1,
            expression='1 + 1'
        )

        lines_out = [
            "print('_equals_start:0')",
            "print(1 + 1)",
            "print('_equals_end:0')",
        ]

        output = python._gen_print_lines(el)
        assert output == lines_out


    def test_preporcess(self):

        lines_in = [
            "1 + 1 #=",
        ]

        lines_out = [
            "1 + 1 #=",
            "print('_equals_start:0')",
            "print(1 + 1)",
            "print('_equals_end:0')",
        ]

        output, el = python.preprocess(lines_in)
        assert el[0].line_num == 0
        assert el[0].expression == '1 + 1'
        assert output == lines_out


if __name__ == '__main__':
    unittest.main()
