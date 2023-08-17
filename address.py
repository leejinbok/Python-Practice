import csv
from hashMap import Hashmap


# defined address class per video on greedy algorithms
class Address:
    def __init__(self, ID, name, text, status):
        self.ID = ID
        self.name = name
        self.text = text
        self.status = status

    def __str__(self):  # overwrite print(address) otherwise print object reference
        return " %s, %s, %s, %s" % (self.ID, self.name, self.text, self.status)


# create load address function -> O(n)
def load_address(filename):
    with open(filename, encoding='utf-8-sig') as file:
        address_data = csv.reader(file, delimiter=',')
        for data in address_data:
            address_id = data[0]
            address_name = data[1]
            address_text = data[2]
            address_status = "loaded"

            # address object
            address = Address(address_id, address_name, address_text, address_status)
            # print(address)

            # insert into hash table
            address_list.append(address)
            # print(f"Added address with ID {address_id} : {address}")


# create address hash
address_hash = Hashmap()
address_list = []
