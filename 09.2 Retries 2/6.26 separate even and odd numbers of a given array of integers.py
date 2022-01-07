arson = [5,4,3,2,6,7]
newson = []

for num in arson:
    if num%2 == 0:
        newson.insert(0, num)
    else:
        newson.insert(-1, num)

print(newson)