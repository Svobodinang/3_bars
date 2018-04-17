import json
import math


def load_data(filepath):
    with open(filepath, encoding="utf-8", newline="") as f:
    	return json.load(f)


def get_biggest_bar(data_bars):
    bars = data_bars["features"]

    max_bar = max(bars, key=lambda x: x["properties"]["Attributes"]["SeatsCount"])

    return max_bar


def get_smallest_bar(data_bars):
    bars = data_bars["features"]

    min_bar = min(bars, key=lambda x: x["properties"]["Attributes"]["SeatsCount"])

    return min_bar


def get_bar_coordinate():
    try:
        coordinate = float(input("введите координатy: "))
    except ValueError:
        print("Это не число!")
    return coordinate

def formula(x, y, z):
    return math.sqrt(pow(x, 2) + pow(y, 2)) - z

def get_closest_bar(data_bars, longitude, latitude):
    our_bar_distance_to_zero = math.sqrt(pow(longitude, 2) + pow(latitude, 2))

    bars = data_bars["features"]

    closest_bar = min(bars, key=lambda x: 
        formula(x["geometry"]["coordinates"][0], x["geometry"]["coordinates"][1], our_bar_distance_to_zero))

    return closest_bar


if __name__ == "__main__":
    pass
