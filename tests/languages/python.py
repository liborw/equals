import unittest
from equals.languages import python


class TestPythonModule(unittest.TestCase):

    def test_process_equals_line(self):

        start, end, expr = python._parse_equals_line('1 + 1 #= ')
        assert (start, end, expr) == (8, -1, '1 + 1')




if __name__ == '__main__':
    unittest.main()
