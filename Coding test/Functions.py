from math import sin, cos, acos, radians
from operator import itemgetter

OFFICE_LATITUDE = 53.339428
OFFICE_LONGITUDE = -6.257664
RADIUS_OF_EARTH_IN_KM = 6371


def get_great_circle_distance(latitude, longitude):
    office_lat_radians, office_long_radians, latitude_radians, longitude_radians = get_degrees_to_radians(
        latitude, longitude)
    central_angle = acos(sin(office_lat_radians) * sin(latitude_radians) + cos(office_lat_radians) *
                         cos(latitude_radians) * cos(office_long_radians - longitude_radians))
    great_circle_distance = RADIUS_OF_EARTH_IN_KM * central_angle
    return great_circle_distance


def get_degrees_to_radians(latitude, longitude):
    degrees_to_radians = map(radians, [OFFICE_LATITUDE, OFFICE_LONGITUDE, latitude, longitude])
    return degrees_to_radians


def get_sorted_guest_list_by_user_id(guest_list, sorting_index):
    guest_list = sorted(guest_list, key=itemgetter(sorting_index))
    return guest_list
