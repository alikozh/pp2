import json

car = {
    "make": "subaru",
    "model": "impreza",
    "year": 1995
}

print(car["model"])
print(" ")

for key in car:
    print(car[key])

print(" ")

for key, value in car.items():
    print(key, ":", value)

print(" ")

for value in car.values():
    print(value)
    

car_json = json.dumps(car)

print(car_json)
print(type(car_json))