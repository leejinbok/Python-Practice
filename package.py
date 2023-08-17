import csv
from hashMap import Hashmap


class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
        self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.notes, self.status)


# create load package function
def load_package(filename):
    with open(filename, encoding='utf-8-sig') as file:
        package_data = csv.reader(file, delimiter=',')
        for data in package_data:
            package_id = data[0]
            package_address = data[1]
            package_city = data[2]
            package_state = data[3]
            package_zip = data[4]
            package_deadline = data[5]
            package_weight = data[6]
            package_notes = data[7]
            package_status = "loaded"

            # package object
            package = Package(package_id, package_address, package_city, package_state, package_zip, package_deadline,
                              package_weight, package_notes, package_status)
            # print(package)

            # add to hashtable
            package_hash.add(package_id, package)
            # print(f"Added package ID: {package_id} : {package}")


# create package hash
package_hash = Hashmap()
