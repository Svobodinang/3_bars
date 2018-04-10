import json
import math

def load_data(filepath):
	with open(filepath, encoding='utf-8', newline='') as f:
	    return json.load(f)


def get_biggest_bar(data):
    a = []
    name = []
    ii = 0
    for d in data["features"]:
    	a.append(d["properties"]["Attributes"]["SeatsCount"])
    	name.append(d["properties"]["Attributes"]["Name"])

    for d in data["features"]:
    	if (a[ii] == max(a)):
    		break
    	else:
    	    ii+=1

    return name[ii]

def get_smallest_bar(data):
    a = []
    name = []
    ii = 0
    for d in data["features"]:
    	a.append(d["properties"]["Attributes"]["SeatsCount"])
    	name.append(d["properties"]["Attributes"]["Name"])

    for d in data["features"]:
    	if (a[ii] == min(a)):
    		break
    	else:
    	    ii+=1

    return name[ii]

def get_closest_bar(data, longitude, latitude):
    a = [] #массив данных
    b = [] #массив расстояний до нуля исходных данных
    c = [] #массив для сравнения
    name = [] #массив названий
    m = 2 #количество координат
    ii = 0

    x = float(input("введите координатy x: "))
    y = float(input("введите координатy y: "))

    z = math.sqrt(pow(x, 2) + pow(y, 2)) #растояние до нуля введенных данных

    for i in data["features"]:
    	a.append([])
    	for j in range(m):
    		a[ii].append(i["geometry"]["coordinates"][j])
    	b.append(math.sqrt(pow(a[ii][0], 2) + pow(a[ii][1], 2)))
    	c.append(b[ii] - z)
    	name.append(i["properties"]["Attributes"]["Name"])
    	ii+=1

    ii = 0 

    for i in data["features"]:
    	if (c[ii] == min(c)):
    		break
    	else:
    	    ii+=1
    return name[ii]

if __name__ == '__main__':
    pass