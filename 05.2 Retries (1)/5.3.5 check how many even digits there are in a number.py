def check_evens(n):
    nlist = list(str(n))
    
#    for j in range(0, len(nlist)):
#        nlist[j] = int(nlist[j])

    nlist = [int(j) for j in nlist]

    counter = 0
    for i in range(0,len(nlist)):
        if nlist[i] % 2 == 0:
            counter += 1
    
    return counter


print(check_evens(2244446666661515151588888888))