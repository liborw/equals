import unittest
from equals import cli

test_code_in = """

1 + 1 #=

a = 1
b = a + 1 #=

"""

test_code_out = """

1 + 1 #= 2

a = 1
b = a + 1 #= 2

"""

test_updates = [
    (2, 8, -1, "2"),
    (5,12, -1, "2"),
]

test_lines_in = test_code_in.split('\n')
test_lines_out = test_code_out.split('\n')


class TestCliModule(unittest.TestCase):

    def test_apply_updates_min(self):
        lines_out = cli.apply_updates([''], [(0, 0, -1, "test")])
        assert [' test'] == lines_out

    def test_apply_updates_middle(self):
        lines_out = cli.apply_updates(['1 + 1 #=  # val'], [(0, 8, 10, "2")])
        assert ['1 + 1 #= 2 # val'] == lines_out

    def test_apply_updates(self):
        lines_out = cli.apply_updates(test_lines_in, test_updates)
        assert test_lines_out == lines_out


if __name__ == '__main__':
    unittest.main()
