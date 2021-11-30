def f1(a):
    hums = 0
    for i in a:
        if i%2==0 and i>8:
            hums+=1
    
    return hums

print(f1([13,7,4,16,3,12,8]))