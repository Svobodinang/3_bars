import json
import math
import sys
import os


def load_data(filepath):
    try:
        with open(filepath, encoding="utf-8") as bars:
            object_bars = json.load(bars)
        object_bars_features = object_bars["features"]
        return object_bars_features
    except json.decoder.JSONDecodeError:
        return None


def output_name_bar(property_bar, bar):
    print(property_bar, bar["properties"]["Attributes"]["Name"])


def get_biggest_bar(bars):
    max_bar = max(
        bars, key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return max_bar


def get_smallest_bar(bars):
    min_bar = min(
        bars, key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return min_bar


def get_user_coordinate():
    try:
        coordinate = float(input("введите координатy: "))
        return coordinate
    except ValueError:
        print("ВЫ ВВЕЛИ НЕ ЧИСЛО! Повторите попытку выполнение программы")
        return None


def search_distance_from_user_to_bar(x, y, compared_value):
    return math.sqrt(pow(x, 2) + pow(y, 2)) - compared_value


def get_closest_bar(bars, longitude, latitude):
    our_distance_to_zero = math.sqrt(pow(longitude, 2) + pow(latitude, 2))

    closest_bar = min(
        bars, key=lambda x: search_distance_from_user_to_bar(
            x["geometry"]["coordinates"][0],
            x["geometry"]["coordinates"][1],
            our_distance_to_zero))

    return closest_bar


def check_json_file(path):
    if not os.path.isfile(path):
        print("Такого файла не сущесвтует")
        return None
    elif load_data(sys.argv[1]) is None:
        print("В файле не json тект")
        return
    else:
        return "ok"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Вы не ввели путь к файлу с данными")

    if check_json_file(sys.argv[1]) is None:
        exit()

    data_bars = load_data(sys.argv[1])
    output_name_bar("Самый большой бар: ", get_biggest_bar(data_bars))
    output_name_bar("Самый маленький бар: ", get_smallest_bar(data_bars))
    longitude = get_user_coordinate()
    if longitude is None:
        exit()
    latitude = get_user_coordinate()
    if latitude is None:
        exit()
    output_name_bar("Ближайший бар: ", get_closest_bar(
        data_bars,
        longitude,
        latitude
    ))
