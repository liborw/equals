import unittest
from equals import utils


test_text_in = """
_equals_start:2
10
_equals_end:2
dsafs
fasdfa

_equals_start:3
10
_equals_end:3
"""
test_lines_in = test_text_in.split('\n')

test_text_in_multiline = """
_equals_start:2
10
20
_equals_end:2
"""
test_lines_in_multiline = test_text_in_multiline.split('\n')

class TestUtilsModule(unittest.TestCase):

    def test_process_script_output(self):
        output = list(utils.process_script_output(test_lines_in))
        assert output == [(2, ["10"]), (3, ["10"])]

    def test_process_script_output_multiline(self):
        output = list(utils.process_script_output(test_lines_in_multiline))
        assert output == [(2, ["10", "20"])]



if __name__ == '__main__':
    unittest.main()
