import re

with open("7.28 grades.txt") as file:
    content = file.read()

pattern = r"\b\d+\.\d+\b"
grades = re.findall(pattern, content)

sumson = 0
for num in grades:
    sumson += float(num)

print(round(  sumson/len(grades), 2  ))