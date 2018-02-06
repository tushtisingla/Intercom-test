import json
from pprint import pprint
from Functions import *

MAX_CUSTOMER_DISTANCE_IN_KM = 100
USER_ID_INDEX = 1
CUSTOMER_LIST_FILE = "customer_list.txt"


class CustomerRecords:

    @staticmethod
    def output_guest_list():
        guest_list = list()
        with open(CUSTOMER_LIST_FILE) as file:
            while True:
                json_object = file.readline()
                if not json_object:
                    break
                json_object_data = json.loads(json_object)
                customer_latitude = float(json_object_data['latitude'])
                customer_longitude = float(json_object_data['longitude'])

                distance_between_office_and_customer = get_great_circle_distance(customer_latitude, customer_longitude)

                if distance_between_office_and_customer <= MAX_CUSTOMER_DISTANCE_IN_KM:
                    guest_list.append([json_object_data['name'], json_object_data['user_id']])

        guest_list = get_sorted_guest_list_by_user_id(guest_list, USER_ID_INDEX)

        pprint(guest_list)


if __name__ == "__main__":
    CustomerRecords.output_guest_list()
