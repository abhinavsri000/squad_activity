from helpers.file_io_helper import parse_file
import unittest
from helpers.parse_arg_helper import parse_args

PATH = './resources/inputs/'

class test_helpers(unittest.TestCase):

    def setUp(self):
        pass

    def test_case_no_input_file(self):
        return self.assertEqual(parse_file(),None)

    def test_case_empty_input_file(self):
        return self.assertEqual(parse_file(PATH+'input0.txt'), None)

    def test_case_valid_input_file(self):
        return self.assertEqual(parse_file(PATH+'input1.txt'), ['Create_parking_lot 6',
        'Park KA-01-HH-1234 driver_age 21',
        'Park PB-01-HH-1234 driver_age 21',
        'Slot_numbers_for_driver_of_age 21',
        'Park PB-01-TG-2341 driver_age 40',
        'Slot_number_for_car_with_number PB-01-HH-1234',
        'Leave 2',
        'Park HR-29-TG-3098 driver_age 39',
        'Vehicle_registration_number_for_driver_of_age 18'])

if __name__ == "__main__":
    unittest.main()
