def minmax(maxray):
    i = 0
    maxnum = maxray[0]
    while i < len(maxray):
        if maxray[i] > maxnum:
            maxnum = maxray[i]
        i+=1
    i = 0
    minnum = maxray[0]
    while i < len(maxray):
        if maxray[i] < minnum:
            minnum = maxray[i]
        i+=1
    
    maxedray = []
    maxedray.append(minnum)
    maxedray.append(maxnum)
    return maxedray


minray = [4,2,8,15,4,-1,7,9,5]
print("Array: ", minray)
print("Result: ", minmax(minray))