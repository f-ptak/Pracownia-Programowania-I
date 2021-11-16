fullboard = [1,2,3,4,5,6,7,8,9,10,11]
checkboard = [1,4,7,5,11,10]
delboard = fullboard.copy()

i = 0
while i < len(delboard):
    j = 0
    while j < len(checkboard):
        if delboard[i] == checkboard[j]:
            del delboard[i]
            i-=1
        j+=1
    i+=1

print("Larger Array - Smaller Array =", end=" ")
for p in range(0, len(delboard)):
    print(delboard[p], end=" ")
