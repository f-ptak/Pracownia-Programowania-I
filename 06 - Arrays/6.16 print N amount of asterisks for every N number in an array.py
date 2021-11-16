def star(n):
    for i in range(0,n):
        return "*"*n 


intnums = [12,6,4,9,3, 10]


for i in range(0,len(intnums)):
    print(f"{intnums[i]}: {star(intnums[i])}")