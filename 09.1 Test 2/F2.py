def f2(a1,a2):
    import re
    pattern = r"\d+"
    first = re.findall(pattern, str(a2))
    second = re.findall(pattern, str(a1))
    
    counter = 0
    for i in range(len(second)):
        for j in range(len(first)):
            if second[i] == first[j]:
                counter+=1
    
    result = ""
    for i in range(counter):
        result += "*"
    
    return result