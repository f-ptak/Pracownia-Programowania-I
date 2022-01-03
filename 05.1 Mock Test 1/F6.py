def rand(fromm, to):
    import random
    value = random.randrange(fromm, to+1)
    if value % 2 == 0 and value % 3 == 0:
        return print(value)
    else:
        rand(fromm,to)
        
        
rand(5,7)