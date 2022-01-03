def f5(c,n):
    import re
    with open("beautybeast.txt") as file:
        
        for i in range(n):
            text = file.readline()
        
        findson = re.findall(c, text)
    
    if len(findson) != 0:
        return True
    else:
        return False