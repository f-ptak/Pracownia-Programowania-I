import json

with open("8.21 euro.json") as file:
    content = json.load(file)

print(f"{'Date':<15} {'Buying Rate':<15} {'Selling Rate'}")
print("============================================")

for rate in content["rates"]:
    print(f"{rate['effectiveDate']:<15} {rate['bid']:<15} {rate['ask']}")