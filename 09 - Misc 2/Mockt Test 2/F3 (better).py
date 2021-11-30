def f3(t):
    import re
    intson = re.findall(r"\b\d{2,3}\b", t)
    
    for i in range(len(intson)):
        intson[i] = int(intson[i])
    
    return sum(intson)

print(f3("Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"))