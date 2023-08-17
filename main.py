import math
import datetime

from address import *
from package import *
from distance import *
from trucks import *
import csv

load_address("./csv/address.csv")
load_package("./csv/package.csv")
load_distance("./csv/distance2.csv")
start_address = address_list[0]


# performs euclidean distance function O(1)
def euclidean_distance(point1, point2):
    if len(point1) != len(point2):
        raise ValueError(f"{point1} and {point2} needs to be of same length for calculation to work")

    distance_squared = sum((a - b) ** 2 for a, b in zip(point1, point2))
    return math.sqrt(distance_squared)


# performs nearest neighbor algorithm - uses O(n) time complexity and O(1) space complexity
def find_nearest_neighbor(query):
    nearest_neighbor_index = None
    nearest_distance = float('inf')

    for i, point in enumerate(float_distance[query]):
        if i != query:
            euc_distance = point
            if euc_distance < nearest_distance:
                nearest_distance = euc_distance
                nearest_neighbor_index = i
    return nearest_neighbor_index


def id_to_address(search):
    row = address_hash.get(search)
    parts = str(row).split(",")
    return parts[2]


def address_to_id(search):
    parts = str(search).split(",")
    return parts[0]


def show_address():
    for i in range(0, 27):
        nearest_neighbor = find_nearest_neighbor(i)
        print(str(nearest_neighbor))


def package_weight(package):
    parts = str(package).split(",")
    return parts[6]


def package_address(package):
    parts = str(package).split(",")
    return parts[1]


def address_text(text):
    parts = str(text).split(",")
    return parts[0], parts[2]


# takes truck object and returns address ID coordinates O(2N * M) complexity
def package_distance(truck: Trucks):
    truck_packages_data = []
    pkg_data = []
    for i in truck.package:
        truck_packages_data.append(package_hash.get(str(i)))
    # add starting point as WGU HUB (address_list[0])
    address_id = [int(address_to_id(address_list[0]))]

    for data in truck_packages_data:
        for address in address_list:
            if package_address(data) == address_text(address)[1]:
                address_id.append(int(address_text(address)[0].strip()))
    # add ending point as WGU HUB (address_list[0])
    address_id.append(int(address_to_id(address_list[0])))
    addr_id = address_coordinates(address_id)

    for pkg_id in truck_packages_data:
        pkg_id = address_to_id(pkg_id)
        pkg_data.append(pkg_id)

    return pkg_data, coordinate_distance(addr_id)


# iterates over the list of numbers and sets up coordinates needed to calculate distance O(N)
def address_coordinates(numbers):
    coordinates = []
    for i in range(len(numbers) - 1):
        coordinates.append(((numbers[i]), (numbers[i + 1])))
    return coordinates


def coordinate_distance(coordinates):
    total_distance = 0
    distance = []
    for i in coordinates:
        distance.append(float_distance[i[0]][i[1]])
        total_distance += float_distance[i[0]][i[1]]

    return distance


def delivered_times(truck: Trucks):
    delivered_time = []
    addr_id = package_distance(truck)
    for i in addr_id:
        distance = float_distance[i[0]][i[1]]
        truck.time += datetime.timedelta(hours=distance / truck.mph)
        delivered_time.append(truck.time)
    return delivered_time


def print_all_package_info(number):
    package_data = []


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

truck1_packages = [34, 14, 15, 16, 19, 20, 21, 40, 4, 30, 8, 1, 39, 13]
truck2_packages = [2, 33, 7, 29, 36, 17, 12, 18, 22, 10, 3, 37, 38, 24]
truck3_packages = [31, 32, 6, 11, 23, 26, 25, 5, 9, 27, 35, 28]

truck1 = Trucks(1, truck1_packages, 18, datetime.timedelta(hours=8))
truck2 = Trucks(2, truck2_packages, 18, datetime.timedelta(hours=8))
truck3 = Trucks(3, truck3_packages, 18, datetime.timedelta(hours=10, minutes=20))


print(package_distance(truck1))
"""
delivered_times(truck1)
delivered_times(truck2)
delivered_times(truck3)
"""
print(truck1.time)
print(truck2.time)
print(truck3.time)

name = package_hash.get("1")
print(name.id)
"""
print(truck1_coordinates)
for items in truck1_data:
    print(find_nearest_neighbor(int(items.strip())))
"""

if __name__ == '__main__':
    nearest_neighbor = find_nearest_neighbor(2)
    hashed_address = address_hash.get(str(nearest_neighbor))
