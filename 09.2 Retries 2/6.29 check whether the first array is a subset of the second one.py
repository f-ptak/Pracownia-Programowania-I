first = [-7, 3, 5, 9, 1]
second = [2, 3, 2, 5, 8, 1, 9, 8, -7, 8, -15, -15]

counter = 0
for num in first:
    if num in second:
        counter += 1

if counter == len(first):
    print("first array is a subset of the second one")
else:
    print("first array is NOT a subset of the second one")