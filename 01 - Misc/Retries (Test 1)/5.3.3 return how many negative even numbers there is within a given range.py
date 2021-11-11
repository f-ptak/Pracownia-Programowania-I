def return_numbers(start,end):
    if start >= -1:
        return 0
    
    even = start
    counter = 0
    
    while even < end:
        if even % 2 == 0 and even < -1:
            print(even, end=" ")
            counter += 1
        even += 1
    
    return counter


print(return_numbers(-16,-9))