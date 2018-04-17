import bars

if __name__ == "__main__":
    print("")
    print("MAX BAR: ", bars.get_biggest_bar(bars.load_data()))
    print("")
    print("MIN BAR: ", bars.get_smallest_bar(bars.load_data()))
    print("")
    print("CLOSEST BAR: ", bars.get_closest_bar(bars.load_data(), bars.get_bar_coordinate(), bars.get_bar_coordinate()))
