import random

with open("7.21 randomnumbers.txt", "w") as file:
    for i in range(50):
        num = random.randint(100,1000)
        file.write(f"{num}\n")