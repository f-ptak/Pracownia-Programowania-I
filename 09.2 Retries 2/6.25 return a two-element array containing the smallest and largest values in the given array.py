def minmax(array):
    small = array[0]
    for i in array:
        if i < small:
            small = i
    
    large = array[0]
    for i in array:
        if i > large:
            large = i
    
    return [small, large]

print(minmax([4,2,8,4,7,9,5]))