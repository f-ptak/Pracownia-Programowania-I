def f5(c):
    import re
    
    counter = 0
    with open("9.0.5 poem.txt") as file:
        for row in file:
            if len( re.findall(c, row.lower()) ) > 0:
                counter += 1
                
    
    return counter

print(f5("m"))