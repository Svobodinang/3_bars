import json
import math
import sys
import os


def load_data(filepath):
    with open(filepath, encoding="utf-8") as data_bar:
        data_bars = json.load(data_bar)
    bars = data_bars["features"]
    return bars


def output_json(bars):
    print(json.dumps(
                     bars["properties"]["Attributes"]["Name"],
                     sort_keys=True, ensure_ascii=False, indent=4))


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
    except ValueError:
        print("ВЫ ВВЕЛИ НЕ ЧИСЛО!!! Повторите попытку ввода координат")
        return get_user_coordinate()
    else:
        return coordinate


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


def input_json_path():
    file_json = sys.argv[1]

    dirname, exname = os.path.splitext(file_json)

    if os.path.isfile(file_json):
        if exname == ".json":
            return file_json
        else:
            print("Данный файл имеет расширение не .json")
            exit(0)
    else:
        print("Такого файла не существует")
        exit(0)


if __name__ == "__main__":
    data_bars = load_data(input_json_path())
    print("САМЫЙ БОЛЬШОЙ БАР:")
    output_json(get_biggest_bar(data_bars))
    print("САМЫЙ МАЛЕНЬКИЙ БАР: ")
    output_json(get_smallest_bar(data_bars))
    print("БЛИЖАЙШИЙ БАР:")
    output_json(get_closest_bar(data_bars,
                                get_user_coordinate(),
                                get_user_coordinate()))
