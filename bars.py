import json
import math
import requests


def load_data(filepath = requests.get("https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json")):
    return filepath.json()


def get_biggest_bar(data_bars):
    bar_size = []
    bar_id = []
    index = 0
    for all_bars in data_bars["features"]:
        bar_size.append(all_bars["properties"]["Attributes"]["SeatsCount"])
        bar_id.append(all_bars["properties"]["RowId"])

    for all_bars in data_bars["features"]:
        if bar_size[index] == max(bar_size):
            break
        else:
            index += 1

    return bar_id[index]


def get_smallest_bar(data_bars):
    bar_size = []
    bar_id = []
    index = 0
    for all_bars in data_bars["features"]:
        bar_size.append(all_bars["properties"]["Attributes"]["SeatsCount"])
        bar_id.append(all_bars["properties"]["RowId"])

    for all_bars in data_bars["features"]:
        if bar_size[index] == min(bar_size):
            break
        else:
            index += 1

    return bar_id[index]

def get_bar_coordinate():
    try:
        coordinate = float(input("введите координатy: "))
    except ValueError:
        print("Это не число!")
    return coordinate


def get_closest_bar(data_bars, longitude, latitude):
    bar_coordinates = []
    bar_distance_to_zero = []
    bars_comparison = []
    bar_id = []
    size_of_coordinates = 2
    index = 0

    our_bar_distance_to_zero = math.sqrt(pow(longitude, 2) + pow(latitude, 2))

    for all_bars in data_bars["features"]:
        bar_coordinates.append([])
        for dex in range(size_of_coordinates):
            bar_coordinates[index].append(all_bars["geometry"]["coordinates"][dex])
        bar_distance_to_zero.append(math.sqrt(pow(bar_coordinates[index][0], 2) + pow(
            bar_coordinates[index][1], 2)))
        bars_comparison.append(bar_distance_to_zero[index] - our_bar_distance_to_zero)
        bar_id.append(all_bars["properties"]["RowId"])
        index += 1

    index = 0

    for all_bars in data_bars["features"]:
        if bars_comparison[index] == min(bars_comparison, key=abs):
            break
        else:
            index += 1

    return bar_id[index]


if __name__ == "__main__":
    pass
