
import unittest
from equals.languages import markdown as lang


class TestMarkdownModule(unittest.TestCase):

    def test_preporcess(self):

        lines_in = [
            "This is a test:",
            "```python",
            "1 + 1 #=",
            "```",
        ]

        lines_out = [
            "1 + 1 #=",
            "print('_equals_start:2')",
            "print(1 + 1)",
            "print('_equals_end:2')",
        ]

        output, el = lang.preprocess(lines_in)
        assert el[2].line_num == 2
        assert el[2].expression == '1 + 1'
        assert output == lines_out


if __name__ == '__main__':
    unittest.main()
