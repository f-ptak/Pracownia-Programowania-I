cutray = [5,1,9,6,1,15,4,32,7,18,334,2,3,334]
larray = []

for i in range(len(cutray)):
    if (cutray[i] in larray) == False:
        larray.append(cutray[i])

print("\nArray without duplicates:", end=" ")
for p in range(len(larray)):
    print(larray[p], end=" ")

i=0
while i < len(larray)-1:
    j=0
    while j < len(larray)-1:
        if larray[j] > larray[j+1]:
            temp = larray[j+1]
            larray[j+1] = larray[j]
            larray[j] = temp
        j+=1
    i+=1

print("\nResult:", larray[len(larray)-2])
