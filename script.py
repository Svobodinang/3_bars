import bars

print(bars.get_biggest_bar(bars.load_data("bars_library.json")))

print(bars.get_smallest_bar(bars.load_data("bars_library.json")))

longi = float(input("введите координатy x: "))
lati = float(input("введите координатy y: "))

print(bars.get_closest_bar(bars.load_data("bars_library.json"), longi, lati))





