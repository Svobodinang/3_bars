import json
import math


def load_data(filepath):
    with open(filepath, encoding='utf-8', newline='') as f:
        return json.load(f)


def get_biggest_bar(data_bars):
    size = []
    name_bar = []
    index = 0
    for features in data_bars["features"]:
        size.append(features["properties"]["Attributes"]["SeatsCount"])
        name_bar.append(features["properties"]["Attributes"]["Name"])

    for features in data_bars["features"]:
        if size[index] == max(size):
            break
        else:
            index += 1

    return name_bar[index]


def get_smallest_bar(data_bars):
    size = []
    name_bar = []
    index = 0
    for features in data_bars["features"]:
        size.append(features["properties"]["Attributes"]["SeatsCount"])
        name_bar.append(features["properties"]["Attributes"]["Name"])

    for features in data_bars["features"]:
        if size[index] == min(size):
            break
        else:
            index += 1

    return name_bar[index]


def get_closest_bar(data_bars, longitude, latitude):
    coordinates = []
    distance = []
    comparison = []
    name_bar = []
    size_of_coordinates = 2
    index = 0

    our_comparison = math.sqrt(pow(longitude, 2) + pow(latitude, 2))

    for features in data_bars["features"]:
        coordinates.append([])
        for dex in range(size_of_coordinates):
            coordinates[index].append(features["geometry"]["coordinates"][dex])
        distance.append(math.sqrt(pow(coordinates[index][0], 2) + pow(
            coordinates[index][1], 2)))
        comparison.append(math.fabs((distance[index] - our_comparison)))
        name_bar.append(features["properties"]["Attributes"]["Name"])
        index += 1

    index = 0

    for features in data_bars["features"]:
        if comparison[index] == min(comparison):
            break
        else:
            index += 1

    return name_bar[index]


if __name__ == '__main__':
    pass
