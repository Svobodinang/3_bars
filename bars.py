import json
import math
import sys
import os


def load_data(filepath):
    try:
        with open(filepath, encoding="utf-8") as json_file:
            decoded_json_file = json.load(json_file)
        bars = decoded_json_file["features"]
        return bars
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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Вы не ввели путь к файлу с данными")
    elif not os.path.isfile(sys.argv[1]):
        exit("Такого файла не существует")

    data_bars = load_data(sys.argv[1])
    if data_bars is None:
        exit("В файле не json текст")

    output_name_bar("Самый большой бар: ", get_biggest_bar(data_bars))
    output_name_bar("Самый маленький бар: ", get_smallest_bar(data_bars))
    longitude = get_user_coordinate()
    latitude = get_user_coordinate()
    if (longitude is None) or (latitude is None):
        exit("Введенные координаты содержат не только цифры! Повторите ввод")

    output_name_bar("Ближайший бар: ", get_closest_bar(
        data_bars,
        longitude,
        latitude
    ))
