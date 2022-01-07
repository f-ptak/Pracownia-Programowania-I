arson = [5,1,9,6,1]

large = arson[0]
for num in arson:
    if num > large:
        large = num

small = arson[0]
for num in arson:
    if num < small:
        small = num

print(large - small)