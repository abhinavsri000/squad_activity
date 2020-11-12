from controllers._query_manager import query_manager
import unittest
from entities.parking_lot import Parking_Lot
from entities.driver import Driver

class test_query_manager(unittest.TestCase):

    def set_up(self):
        pass

    def test_get_registration_from_age_no_slots(self):
        return self.assertEqual(query.get_registration_no_from_age(parking_lot,21),[])

    def test_get_registration_from_age_with_slots(self):
        return self.assertEqual(query.get_registration_no_from_age(parking_lot,23),['TEST_REG_NO'])

if __name__ == "__main__":
    parking_lot = Parking_Lot()
    capa = parking_lot.allocate_parking_lot(10)
    driver = Driver(23)
    vehicle = parking_lot.park_vehicle('TEST_REG_NO',driver)
    query = query_manager()
    unittest.main()
