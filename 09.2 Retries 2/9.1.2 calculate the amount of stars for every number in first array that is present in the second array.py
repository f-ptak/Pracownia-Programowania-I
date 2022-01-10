def f2(a1, a2):
    stars = ""
    
    onecheck = []
    for num in a1:
        if num not in onecheck:
            onecheck.append(num)
    
    for fir in onecheck:
        for sec in a2:
            if sec == fir:
                stars += "*"
    
    return stars

print( f2([10,20,38],[14,9,10,31,20]) )
print( f2([8,5,5,4,6],[3,2,5,7,4,1,4,6]) )