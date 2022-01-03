def f4(d,n):
    counter = 0
    for dic in d:
        if dic["age"] > n:
            counter+=1
    
    return counter