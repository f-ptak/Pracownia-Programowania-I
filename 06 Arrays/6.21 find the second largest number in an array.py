def find_largest(array):
    i=0
    largest = array[0]
    while i < len(larray):
        if array[i] > largest:
            largest = array[i]
        i+=1
    return largest

larray = [5,1,9,6,1]

print("Array:", end=" ")
for p in range(len(larray)):
    print(larray[p], end=" ")

first = find_largest(larray)

j=0
while j <len(larray):
    if larray[j] == first:
        del larray[j]
        j-=1
    j+=1

second = find_largest(larray)

print("\nResult:", second)