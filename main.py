import hashMap
import csv


def main():
    pass

#create load address function
def load_address(filename):
    with open(filename, encoding='utf-8-sig') as file:
        address_data = csv.reader(file, delimiter=',')
        for data in address_data:
            address_id = data[0]
            address_name = data[1]
            address_text = data[2]
            address_status = "loaded"

            #address object

def load_distance(filename):
    with open(filename, encoding='utf-8-sig') as file:
        distance_data = csv.reader(file, delimiter=',')
        for line in distance_data:
            print(line)


if __name__ == '__main__':
    address_csv = "./csv/address.csv"
    load_address(address_csv)
    distance_csv = "./csv/distance.csv"
