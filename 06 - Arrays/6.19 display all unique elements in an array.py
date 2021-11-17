# 3 5 1 9
ogray = [2,3,2,5,8,1,9,8,-7,8,-15,-15]
uniray = ogray.copy()
lastray = []

print("Array:", end=" ")
for p in range(len(ogray)):
    print(ogray[p], end=" ")

for n in range(len(uniray)):
    counter = ogray.count(uniray[n])
    if counter == 1:
        lastray.append(uniray[n])

print("\nUnique elements:", end=" ")
for p in range(len(lastray)):
    print(lastray[p], end=" ")
