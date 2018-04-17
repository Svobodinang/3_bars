import json
import math


def load_data(filepath):
    with open(filepath, encoding="utf-8", newline="") as bars:
        return json.load(bars)


def output_json(data):
    print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4))


def get_biggest_bar(data_bars):
    bars = data_bars["features"]

    max_bar = max(
        bars, key=lambda x: x["properties"]["Attributes"]["SeatsCount"])
    
    output_json(max_bar)


def get_smallest_bar(data_bars):
    bars = data_bars["features"]

    min_bar = min(
        bars, key=lambda x: x["properties"]["Attributes"]["SeatsCount"])

    output_json(min_bar)


def get_user_coordinate():
    try:
        coordinate = float(input("введите координатy: "))
    except Exception:
        print("ЭТО ИСКЛЮЧЕНИЕ: ВЫ ВВЕЛИ НЕ ЧИСЛО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return coordinate


def search_distance_from_user_to_bar(x, y, compared_value):
    return math.sqrt(pow(x, 2) + pow(y, 2)) - compared_value


def get_closest_bar(data_bars, longitude, latitude):
    our_distance_to_zero = math.sqrt(pow(longitude, 2) + pow(latitude, 2))

    bars = data_bars["features"]

    closest_bar = min(
        bars, key=lambda x: search_distance_from_user_to_bar(
            x["geometry"]["coordinates"][0],
            x["geometry"]["coordinates"][1], 
            our_distance_to_zero))

    output_json(closest_bar)


if __name__ == "__main__":
	filepath = input("введите путь к файлу: ")
	filepath
	data = load_data(filepath)
	print("САМЫЙ БОЛЬШОЙ БАР:")
	get_biggest_bar(data)
	print("САМЫЙ МАЛЕНЬКИЙ БАР: ")
	get_smallest_bar(data)
	print("БЛИЖАЙШИЙ БАР:")
	get_closest_bar(data, get_user_coordinate(), get_user_coordinate())