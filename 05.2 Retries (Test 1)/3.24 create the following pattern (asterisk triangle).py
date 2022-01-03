def create_asterisks():
    i = 0
    while i <= 5:
        print(i*"*")
        i+=1
    while i > 0:
        print(i*"*")
        i-=1
    
    j = 0
    for j in range(1,6):
        print(j*"o")
    for j in range(4,0,-1):
        print(j*"o")


create_asterisks()