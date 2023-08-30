import datetime

from address import *
from package import *
from distance import *
from trucks import *


load_address("./csv/address.csv")
load_package("./csv/package.csv")
load_distance("./csv/distance2.csv")
start_address = address_list[0]


# function to load packages onto trucks given a parameter of package list
# Time and space complexity of O(n)
def load_packages(packages: list):
    # time and space complexity of O(1)
    truck_items = []
    # time and space complexity of O(n)
    for items in packages:
        # time and space complexity of O(1)
        truck_items.append(package_hash.get(items))
    # time and space complexity of O(1)
    return truck_items


# performs a search to find matching address text between address and packages given Package object
# returns address ID if found; None if not found
# time and space complexity of O(n)
def get_address_id_for_package(package: Package):
    # time and space complexity of O(n)
    for address in address_list:
        # time and space complexity of O(1)
        if package.address == address.text:
            # time and space complexity of O(1)
            return address.id
    # time and space complexity of O(1)
    return None


# performs a function to return the distance between two points given integer parameters point1 and point2
# time complexity of O(1)
def distance_between(point1: int, point2: int):
    # time and space complexity of O(1)
#    print(point1, point2)
    # time and space complexity of O(1)
    distance = float_distance[point1][point2]
    # time and space complexity of O(1)
    return distance


# algorithm to deliver packages with input parameter of Truck object
# Time and space complexity of O(n^2)
def truck_deliver_package(truck: Trucks):
    deliver_addr_list = []
    truck_package_list = []
    truck_package_address_list = []
    total_distance = 0

    for package in truck.package:
        truck_package_list.append(package.id)
    truck_packages = truck.package

    for package in truck.package:
        truck_package_address_list.append(get_address_id_for_package(package))
    current_location = 0

    while len(truck_packages) > 0:
        min_value = 99
        nearest_address_id = -1
        delivery_package = None

        for item in truck_packages:
            package_address_id = get_address_id_for_package(item)
            distance = distance_between(current_location, package_address_id)
            print(distance)
#            print(truck_package_list)
#            print(truck_package_address_list)
            if distance < min_value:
                min_value = distance
                nearest_address_id = package_address_id
                delivery_package = item
        current_location = nearest_address_id

        print(f"package {delivery_package.id} was delivered to address node {nearest_address_id}; "
              f"\ndistance traveled was {min_value} and took {datetime.timedelta(hours=min_value/truck.mph)} minutes")
        deliver_addr_list.append(f"{delivery_package.id}, {nearest_address_id}, {min_value}")
        truck_packages.remove(delivery_package)
        truck_package_list.remove(delivery_package.id)
        truck_package_address_list.remove(nearest_address_id)
        total_distance += min_value

        print(truck_package_list)
        print(truck_package_address_list)
        print(f"total traveled distance: {total_distance:.2f} miles")
    distance = distance_between(current_location, 0)
    print(distance + total_distance)
    return deliver_addr_list

"""
# function to calculate delivered times
def delivered_times(truck: Trucks, addr_id):
    delivered_time = []
    for i in addr_id:
        distance = float_distance[i[0]][i[1]]
        truck.time += datetime.timedelta(hours=distance / truck.mph)
        delivered_time.append(truck.time)
    return delivered_time
"""

"""
while True:
    user_input = input("Please select a number from the following options!\n"
                       "1. Print all package status\n"
                       "2. Print all times\n"
                       "3. Print all miles\n"
                       "4. Get information about a single package\n"
                       "5. Exit program.\n")
    if user_input == "5":
        break
"""


truck1_packages = [27, 35, 29, 7, 1, 13, 39, 30, 8, 31, 40, 4, 37, 34]
truck2_packages = [18, 19, 36, 3, 20, 21, 38, 14, 16, 15]
truck3_packages = [28, 6, 32, 9, 5, 25, 26, 2, 33, 11, 17, 12, 24, 23, 10, 22]


truck1 = Trucks(1, load_packages(truck1_packages), 18, datetime.timedelta(hours=8))
truck2 = Trucks(2, load_packages(truck2_packages), 18, datetime.timedelta(hours=8))
truck3 = Trucks(3, load_packages(truck3_packages), 18, datetime.timedelta(hours=10, minutes=20))


if __name__ == '__main__':
    a= truck_deliver_package(truck1)
    print(a)