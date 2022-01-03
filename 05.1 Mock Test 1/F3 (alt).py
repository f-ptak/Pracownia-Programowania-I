def max4v2(m1,m2,m3,m4):
    num = (m1,m2,m3,m4)
    j = 0
    for i in range(0,4):
        if num[i] > j:
            j = num[i]
    print(j)

max4v2(4,16,7,2)