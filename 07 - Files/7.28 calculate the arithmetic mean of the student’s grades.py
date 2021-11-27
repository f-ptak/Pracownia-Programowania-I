import re

with open("7.28 grades.txt") as file:
    readfile = file.read()
    grades = re.findall("[0-9].[0-9]", readfile)
    
    floatgrades = []
    for val in grades:
        floatgrades.append(float(val))
    
    mean = sum(floatgrades)/len(floatgrades)
    
    print(f"{mean:.2f}")