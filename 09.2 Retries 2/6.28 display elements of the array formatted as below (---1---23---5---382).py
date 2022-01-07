import random

arson = []

for i in range(8):
    arson.append(random.randint(1,999))

print("----------------------------------------")
print("|", end="")

for i in range(8):
    print(f"{arson[i]:>3}|", end=" ")

print("\n----------------------------------------")