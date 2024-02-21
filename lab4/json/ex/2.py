import json

car_json = '{"make": "Subaru", "model": "Impreza", "year": 1995}'

print(type(car_json))

car = json.loads(car_json)

print(type(car))

key = input()
print(car[key])

for key in car:
    print(car[key])