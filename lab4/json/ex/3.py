import json

car = {
    "make": "subaru",
    "model": "impreza",
    "year": 2000
}

with open("car.json", "w") as file:
    json.dump(car, file, indent=4)  