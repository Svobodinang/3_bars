import json
import math
import sys


def load_data(filepath):
    with open(filepath, encoding="utf-8") as data_bar:
        data_bars = json.load(data_bar)
    bars = data_bars["features"]
    return bars


def output_name_bar(find_property_bar):
    id, bars = find_property_bar
    print(id, bars["properties"]["Attributes"]["Name"])


def get_biggest_bar(bars):
    id = "Самый БОЛЬШОЙ бар: "
    max_bar = max(
        bars, key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return id, max_bar


def get_smallest_bar(bars):
    id = "Самый МАЛЕНЬКИЙ бар: "
    min_bar = min(
        bars, key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    return id, min_bar


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
    id = "БЛИЖАЙШИЙ бар: "
    our_distance_to_zero = math.sqrt(pow(longitude, 2) + pow(latitude, 2))

    closest_bar = min(
        bars, key=lambda x: search_distance_from_user_to_bar(
            x["geometry"]["coordinates"][0],
            x["geometry"]["coordinates"][1],
            our_distance_to_zero))

    return id, closest_bar

def check_json_file():
    try:
        load_data(sys.argv[1])
        return "ok"
    except json.decoder.JSONDecodeError:
        print("В файле не json текст")
        return None
    except IndexError:
        print("Вы не указали путь к файлу")
        return None
    except FileNotFoundError:
        print("Такого файла не существует")
        return None




if __name__ == "__main__":

    if check_json_file()==None:
        exit(0)
    data_bars = load_data(sys.argv[1])
    output_name_bar(get_biggest_bar(data_bars))
    output_name_bar(get_smallest_bar(data_bars))
    x = get_user_coordinate()
    if x!=None:
        y = get_user_coordinate()
        if y!=None:
            output_name_bar(get_closest_bar(data_bars, x, y))
