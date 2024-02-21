import json

file = open("car.json")

cars_json = file.read()

cars = json.loads(cars_json)

cars.append({
    "make": "Audi",
    "model": "Quattro",
    "year": 1982
})

cars_json = json.dumps(cars, indent=4)

file = open("car.json", "w")

file.write(cars_json)
