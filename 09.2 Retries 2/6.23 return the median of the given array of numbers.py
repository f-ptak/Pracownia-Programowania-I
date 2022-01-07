def median(array):
    
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    
    print(array)
    if len(array)%2 != 0:
        return array[len(array)//2]
    else:
        return round(     (array[len(array)//2] + array[(len(array)-1)//2]) /2     , 2)

print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))

print(median([1,0,9,9,4,6]))
print(median([6,8,3,1,4,0,5,7]))