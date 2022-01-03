import json

with open("8.15 student.json", "w") as studfile:
    
    studic = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"},
    "moneyzz???": None
    }
    
    studfile.write(json.dumps(studic, indent=4))