def f1(a,c):
    import re
    findson = re.findall(c, str(a)) 
    return len(findson)