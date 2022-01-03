def f4(d):
    import re
    sd = str(d)
    searchson = re.findall(r"[0-9]+", sd)
    
    valray = []
    for val in searchson:
        if int(val) >=5 and int(val) <=10:
            valray.append(int(val))
    
    return sum(valray)

print(f4({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}))
