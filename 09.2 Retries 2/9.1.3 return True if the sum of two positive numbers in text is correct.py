def f3(t):
    import re
    
    add = re.findall(r"\d+[+]\d+", t)
    result = re.findall(r"[=]\d+", t)
    
    add = add[0].split("+")
    result = result[0].split("=")
    
    if (  int(add[0]) + int(add[1])  ) == int(result[-1]):
        return True
    else:
        return False

print( f3("450+3=453") )
print( f3("4+2229=2233") )
print( f3("5000+801=5802") )