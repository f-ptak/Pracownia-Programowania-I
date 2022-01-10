def f3(t):
    import re
    pattern = r"-?\d+"
    findson = re.findall(pattern, t)
    
    return (int(findson[0]) + int(findson[1])) == int(findson[2])