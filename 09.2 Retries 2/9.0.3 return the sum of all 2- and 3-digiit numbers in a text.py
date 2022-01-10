def f3(t):
    import re
    
    pattern = "\d{2,}"
    digits = re.findall(pattern, t)
    
    sumson = 0
    for val in digits:
        if len(val) == 2 or len(val) == 3:
            sumson += int(val)
    
    return sumson

print(f3("Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"))
print(f3("198fan s372*39338s s10j9f"))