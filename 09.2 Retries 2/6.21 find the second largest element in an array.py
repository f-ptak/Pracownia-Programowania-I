arson = [5,1,9,6,1]
pureson = []

for pos in arson:
    if pos not in pureson:
        pureson.append(pos)

for j in range(len(pureson)-1):
    for i in range(len(pureson)-1):
        if pureson[i] > pureson[i+1]:
            temp = pureson[i]
            pureson[i] = pureson[i+1]
            pureson [i+1] = temp
        
print(pureson[-2])

