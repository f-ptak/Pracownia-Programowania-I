def median(medray):
    i=0
    while i < len(medray)-1:
        j=0
        while j < len(medray)-1:
            if medray[j] > medray[j+1]:
                temp = medray[j+1]
                medray[j+1] = medray[j]
                medray[j] = temp
            j+=1
        i+=1
    
    median = medray[len(medray)//2]
    return median


print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))