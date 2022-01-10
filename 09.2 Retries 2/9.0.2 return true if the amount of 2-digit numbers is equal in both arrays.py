def f2(a1,a2):
    onecount = 0
    for val in a1:
        if len( str(val) ) == 2:
            onecount += 1
    
    twocount = 0
    for val in a2:
        if len( str(val) ) == 2:
            twocount += 1
    
    if onecount == twocount:
        return True
    else:
        return False

print(f2([23,7,16,34],[1,18,79,20,6,111]))