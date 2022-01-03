def disp_rand():
    import random
    i=0
    while i < 20:
        value = random.randint(1,10)
        print(value, end=" ")
        i+=1


disp_rand()