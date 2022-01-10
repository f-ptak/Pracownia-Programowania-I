def f1(a, c):
    import re
    return len(  re.findall(c, str(a))  )

print( f1(["sun","moon","sand"],"n") )
print( f1(["book","moon","poetry","footbal"],"o") )