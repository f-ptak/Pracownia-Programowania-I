def rand(start,end):
    import random
    x = random.randint(start,end)
    if x % 2 == 0 and x % 3 == 0:
        return print(x)
    else:
        rand(start, end)   


rand(1,34)