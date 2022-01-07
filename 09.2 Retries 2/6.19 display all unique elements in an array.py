orison = [2,3,2,5,8,1,9,8]
arson = orison.copy()
unison = []
print(arson)

i = 0
while i < len(arson):
    check = arson[0]
    del arson[0]
    
    if check not in arson:
        unison.append(check)
        i -= 1
    else:
        j = 0
        while j < len(arson):
            if arson[j] == check:
                del arson[j]
                j -= 1
                i -= 1
            j += 1
    i += 1

print(unison)
countson = []

for pos in orison:
    if orison.count(pos) == 1:
        countson.append(pos)

print(countson)