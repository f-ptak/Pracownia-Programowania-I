def occurs(number, array):
    i=0
    while i <len(array):
        if checknum == array[i]:
            return True
        else:
            i+=1


checknum = int(input("Number: "))
checkray = [15, 38, 7, 23, 14]


print("Array:", end=" ")
for p in range(len(checkray)):
    print(checkray[p], end=" ")

if occurs(checknum,checkray) == True:
    print(f"\nResult: number {checknum} appears in the array")
else:
    print(f"\nResult: number {checknum} does not appear in the array")
