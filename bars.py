import json
import math


def load_data(filepath):
	with open(filepath, encoding='utf-8', newline='') as f:
	    return json.load(f)

def get_biggest_bar(data):
    size = []
    name = []
    index = 0
    for d in data["features"]:
    	size.append(d["properties"]["Attributes"]["SeatsCount"])
    	name.append(d["properties"]["Attributes"]["Name"])

    for d in data["features"]:
    	if size[index] == max(size):
    		break
    	else:
    	    index += 1

    return name[index]

def get_smallest_bar(data):
    size = []
    name = []
    index = 0
    for d in data["features"]:
    	size.append(d["properties"]["Attributes"]["SeatsCount"])
    	name.append(d["properties"]["Attributes"]["Name"])

    for d in data["features"]:
    	if size[index] == min(size):
    		break
    	else:
    	    index += 1

    return name[index]

def get_closest_bar(data, longitude, latitude):
    coordinates = [] #массив данных
    distance = [] #массив расстояний до нуля исходных данных
    comparison = [] #массив для сравнения
    name = [] #массив названий
    size_of_coordinates = 2 #количество координат
    index = 0

    z = math.sqrt(pow(longitude, 2) + pow(latitude, 2)) #растояние до нуля введенных данных

    for i in data["features"]:
    	coordinates.append([])
    	for j in range(size_of_coordinates):
    		coordinates[index].append(i["geometry"]["coordinates"][j])
    	distance.append(math.sqrt(pow(coordinates[index][0], 2) + pow(coordinates[index][1], 2)))
    	comparison.append(math.fabs((distance[index] - z)))
    	name.append(i["properties"]["Attributes"]["Name"])
    	index += 1

    index = 0 

    for i in data["features"]:
    	if comparison[index] == min(comparison):
    		break
    	else:
    	    index += 1

    return name[index]

if __name__ == '__main__':
    pass