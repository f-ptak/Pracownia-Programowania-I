def f4(d):
    import re
    sd = str(d)
    searchson = re.findall(r"\b[5-9]\b|\b[1][0]\b", sd)
    print(searchson)
    for i in range(len(searchson)):
        searchson[i] = int(searchson[i])
        
    return sum(searchson)

print(f4({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}))