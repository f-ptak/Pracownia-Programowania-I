import json

with open("8.13 json example.json") as file:
    content = json.load(file)

for key, value in content.items():
    print(f"{key:<10}: {value}")