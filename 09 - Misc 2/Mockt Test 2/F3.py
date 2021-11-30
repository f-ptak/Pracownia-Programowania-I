def f3(t):
# .join()
    unwanted = "!@#$;:!*%)(&^~,."
    cleanson = "".join(j for j in t if j not in unwanted)
# .replace()
#     cleanson = t.replace(",", "")
#     cleanson = cleanson.replace(".", "")
    
    listson = cleanson.split(" ")
    intson = []
    for i in range(len(listson)):
        try:
            listson[i] = int(listson[i])
            intson.append(listson[i])
        except:
            continue
    
    numson = 0
    for num in intson:
        if len(list(str(num))) == 2 or len(list(str(num))) == 3:
            numson+=num
    
    return numson

print(f3("Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"))