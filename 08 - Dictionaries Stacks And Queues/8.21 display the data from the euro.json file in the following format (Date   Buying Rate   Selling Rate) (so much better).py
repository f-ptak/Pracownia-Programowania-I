import json

print("Date: \t\t Buying Rate: \t Selling Rate:")
print("===============================================")

with open("8.21 euro.json", "r") as file:
    data = json.load(file)

for val in data["rates"]:
    print(f"{val['effectiveDate']} \t {val['bid']} \t {val['ask']}")