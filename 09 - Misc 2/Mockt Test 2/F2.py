def f2(a1,a2):
    aones = 0
    atwos = 0
    
    for i in range(len(a1)):
        la1 = list(str(a1[i]))
        if len(la1) == 2:
            aones+=1
    
    for i in range(len(a2)):
        la2 = list(str(a2[i]))
        if len(la2) == 2:
            atwos+=1
            
    if aones == atwos:
        return True
    else:
        return False

print(f2([23,7,16,34],[1,18,79,20,6,111]))