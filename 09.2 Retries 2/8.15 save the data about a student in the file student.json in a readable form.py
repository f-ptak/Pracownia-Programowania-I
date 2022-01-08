import json

student = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": [
        "swimming",
        "excursions"
    ],
    "married": True,
    "phone": {
        "landline": "123444321",
        "mobile": "777888999"
    },
    "moneyzz???": None
}

with open("8.15 student.json", "w") as file:
    json.dump(student, file, indent = 4)