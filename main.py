import heapq
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


# performs nearest neighbor algorithm - uses O(n) time complexity and O(1) space complexity
def find_nearest_neighbor(point, address):
    nearest_neighbor_index = None
    nearest_distance = float('inf')
    point = int(point)

    for i, distance in enumerate(float_distance[point]):
        if distance < nearest_distance and i != point:
            nearest_distance = distance
            nearest_neighbor_index = i
    """    elif i == point:
            nearest_distance = distance
            nearest_neighbor_index = i
            continue
    """

    nearest_point = address[nearest_neighbor_index]
    return nearest_distance, nearest_point




# takes truck object and returns address ID coordinates O(2N * M) complexity
def package_address_id(truck: Trucks):
    address_id = []
    # add starting point as WGU HUB (address_list[0])
    for packages in truck.package:
        for address in address_list:
            if packages.address == address.text:
                address_id.append(address.id)
    # add ending point as WGU HUB (address_list[0])
    return address_id


# iterates over the list of numbers and sets up coordinates needed to calculate distance O(N)
def address_coordinates(numbers):
    coordinates = []
    for i in range(len(numbers) - 1):
        coordinates.append(((numbers[i]), (numbers[i + 1])))
    return coordinates


def coordinate_distance(coordinates):
    distance = []
    for i in coordinates:
        distance.append(float_distance[i[0]][i[1]])
    return distance


def get_id_for_address(package_address):
    # add starting point as WGU HUB (address_list[0])
    for address in address_list:
        if address.text == package_address:
            return address.id
    # add ending point as WGU HUB (address_list[0])
    return None


def distance_between(point1, point2):
    print(point1, point2)
    distance = float_distance[point1][point2]
    return distance


def truck_deliver_package(truck):
    deliver_addr_list = []
    truck_packages = []
    current_location = 0
    truck_packages_address_list = package_address_id(truck)
    for items in truck.package:
        truck_packages.append(items)
        print(items)

    while len(truck_packages_address_list) > 0:
        min_value = 99
        nearest_address_id = -1
        nearest_package = None
        for item in truck_packages_address_list:
   #         min_value, id, nearest_package = min_distance(item, truck)
            package = package_hash.get(item)
            address_id = get_id_for_address(package.address)
            distance = distance_between(item, address_id)
            if distance < min_value:
                min_value = distance
                nearest_address_id = address_id
                nearest_package = item

        print(f"{nearest_address_id} : {min_value} : {nearest_package} : {truck_packages_address_list}")
        deliver_addr_list.append(f"{nearest_address_id}, {min_value}, {nearest_package}")
        print(truck_packages_address_list)
        truck_packages_address_list.remove(nearest_package)
        print(truck_packages_address_list)
        print(deliver_addr_list)

    return deliver_addr_list


def load_packages(packages:list):
    truck_items = []
    for items in packages:
        truck_items.append(package_hash.get(items))
    return truck_items


def delivered_times(truck: Trucks, addr_id):
    delivered_time = []
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

truck1_packages = [27, 35, 29, 7, 1, 13, 39, 30, 8, 31, 40, 4, 37, 34]
truck2_packages = [18, 19, 36, 3, 20, 21, 38, 14, 16, 15]
truck3_packages = [28, 6, 32, 9, 5, 25, 26, 2, 33, 11, 17, 12, 24, 23, 10, 22]


truck1 = Trucks(1, load_packages(truck1_packages), 18, datetime.timedelta(hours=8))
truck2 = Trucks(2, load_packages(truck2_packages), 18, datetime.timedelta(hours=8))
truck3 = Trucks(3, load_packages(truck3_packages), 18, datetime.timedelta(hours=10, minutes=20))


"""
def find_next_nearest(current_address, addresses, truck, distances):
    nearest_distance = float('inf')
    next_nearest_address = None
    address = package_address_id(truck).copy()


    for items in addresses:
        distances = find_nearest_neighbor(current_address, address)
        if distances[0] <= nearest_distance:
            nearest_distance = distances[0]
            next_nearest_address = items
    return next_nearest_address


def package_algorithm(truck:Trucks):
    package_values = []
    address = sorted(package_address_id(truck).copy())
    current_address = address[0]
    print(address)
    a = (address_coordinates(address))
    print(a)

    while current_address:
        distances = find_nearest_neighbor(current_address, address_list)
        nearest_id = distances[1].id
        nearest_distance = distances[0]

        nearest_package = None
        for package in address:
            if package == nearest_id:
                nearest_package = package
                address.remove(package)
                break

        if nearest_package:
            # Update the current address and add the package to the route
            current_address = nearest_id
            package_values.append(nearest_package)
        else:
            # If no nearest package is found, find the next nearest
            current_address = find_next_nearest(current_address, address, truck, distances)
            if current_address is None:
                break  # No more packages left
    return package_values


print(truck1_coordinates)
for items in truck1_data:
    print(find_nearest_neighbor(int(items.strip())))
"""

if __name__ == '__main__':
    a= truck_deliver_package(truck1)
    print(a)