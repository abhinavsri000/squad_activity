import unittest
from parking_project.helpers.file_io_helper import parse_file

class helper_tests(unittest.TestCase):

    def test_check_for_no_input_file(self):
        output = parse_file('./test_resources/inputs/input0.txt')


if __name__ == "__main__":
    unittest.main()
