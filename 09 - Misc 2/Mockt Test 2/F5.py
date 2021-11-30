def f5(c):
    import re
    with open("poem.txt") as file:
        
        counter = 0
        for line in file:
            if len(re.findall(c.upper(), line.upper())) != 0:
                counter +=1
    
    return counter

print(f5("m"))