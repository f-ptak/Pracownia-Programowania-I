def f4(n1,n2,n3):
    numbers = (n1,n2,n3)
    i = 0
    j = 0
    while i<3:
        if numbers[i] >= j:
            j = numbers[i]
        i+=1
    n = 2
    m = j
    while n>=0:
        if numbers[n] <= m:
            m = numbers[n]
        n-=1
    return j-m