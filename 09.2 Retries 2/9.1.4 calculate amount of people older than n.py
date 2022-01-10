def f4(d,n):
    counter = 0
    
    for person in d:
        if person["age"] > n:
            counter += 1
    
    return counter

print(  f4([{"name":"Peter","age":30},{"name":"Ann","age":22},{"name":"Mark","age":28}],25)  )
print(  f4([{"name":"Peter","age":16},{"name":"Ann","age":18}],17)  )