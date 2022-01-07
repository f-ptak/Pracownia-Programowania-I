first = [1,2,3,4,5,6,7,8,9,10,11]
second = [1,4,7,5,11,10]

for i in range(len(first)):
    if first[i] not in second:
        print(first[i], end=" ")