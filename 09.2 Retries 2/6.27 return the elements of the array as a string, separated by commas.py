def separate(arson):
    commas = ""
    for i in range(len(arson)):
        if i < len(arson)-1:
            commas += str(arson[i]) + ", "
        else:
            commas += str(arson[i])
    
    return commas

print(separate([5,4,3,2,6,5]))