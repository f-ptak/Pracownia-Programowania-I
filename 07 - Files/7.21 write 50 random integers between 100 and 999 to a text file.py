import random

with open("7.21 random numbers.txt", "w") as ranbers:
    for i in range(0,50):
        ranbers.write(str(random.randint(100,999))+"\n")