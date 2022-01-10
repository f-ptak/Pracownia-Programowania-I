def f4(d):
    import re
    
# returning only the numbers in values (arrays), not in keys
#     sumson = 0
#     for arr in d:
#         for dig in d[arr]:
#             if 5 <= dig <= 10:
#                 sumson += dig
#     return sumson
    
    pattern = "\d+"
    digs = re.findall(pattern, str(d))
    
    sumson = 0
    for i in range(len(digs)):
        if 5 <= int(digs[i]) <= 10:
            sumson += int(digs[i])
    
    return sumson

print( f4({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}) )