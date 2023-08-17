import csv


def load_distance(filename):
    with open(filename, encoding='utf-8-sig') as file:
        distance_data = csv.reader(file, delimiter=',')
        for row in distance_data:
            float_values = [float(value) for value in row]
            float_distance.append(float_values)


float_distance = []
