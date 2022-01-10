def f2(a1,a2):
    import re
    pattern = r"\d+"
    fir = re.findall(pattern, str(a2))
    second = re.findall(pattern, str(a1))

    first = []
    for i in range(len(fir)):
        if (fir[i] not in first):
            first.append(fir[i])
    
    counter = 0
    for i in range(len(second)):
        for j in range(len(first)):
            if second[i] == first[j]:
                counter+=1
    
    result = ""
    for i in range(counter):
        result += "*"
    
    return result

print(f2([10,20,38],[14,9,10,31,20]))
print(f2([8,5,5,4,6],[3,2,5,7,4,1,4,6]))