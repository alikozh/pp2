import json

with open("car.json", "r") as file:
    cars = json.load(file)

cars.append({
    "make": "Audi",
    "model": "A8",
    "year": 2012
})

with open("car.json", "w") as file:
    json.dump(cars, file, indent=4)