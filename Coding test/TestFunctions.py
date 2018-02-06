import unittest
from Functions import *

DECIMAL_PRECISION_FOR_DISTANCE = 1
DECIMAL_PRECISION_FOR_DEGREE_TO_RADIAN = 6


class TestFunctions(unittest.TestCase):

    def test_get_great_circle_distance(self):
        great_circle_distance = get_great_circle_distance(54.1225, -8.143333)
        great_circle_distance = round(great_circle_distance, DECIMAL_PRECISION_FOR_DISTANCE)
        self.assertEqual(great_circle_distance, 151.5)

    def test_get_degrees_to_radians(self):
        office_lat_radians, office_long_radians, latitude_radians, longitude_radians = get_degrees_to_radians(
            54.1225, -8.143333)

        office_lat_radians = round(office_lat_radians, DECIMAL_PRECISION_FOR_DEGREE_TO_RADIAN)
        office_long_radians = round(office_long_radians, DECIMAL_PRECISION_FOR_DEGREE_TO_RADIAN)
        latitude_radians = round(latitude_radians, DECIMAL_PRECISION_FOR_DEGREE_TO_RADIAN)
        longitude_radians = round(longitude_radians, DECIMAL_PRECISION_FOR_DEGREE_TO_RADIAN)

        self.assertEqual(office_lat_radians, 0.930949)
        self.assertEqual(office_long_radians, -0.109217)
        self.assertEqual(latitude_radians, 0.944616)
        self.assertEqual(longitude_radians, -0.142128)

    def test_get_sorted_guest_list_by_user_id(self):
        unsorted_list = [['Tushti', 6], ['Aashish', 9], ['Amber', 3]]
        sorted_list = get_sorted_guest_list_by_user_id(unsorted_list)
        self.assertEqual(sorted_list, [['Amber', 3], ['Tushti', 6], ['Aashish', 9]])


if __name__ == "__main__":
    TestFunctions.test_get_great_circle_distance()
    TestFunctions.test_get_degrees_to_radians()
    TestFunctions.test_get_sorted_guest_list_by_user_id()