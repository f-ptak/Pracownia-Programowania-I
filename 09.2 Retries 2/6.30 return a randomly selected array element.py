def rand_elem(array):
    import random
    
    num = random.randint(0,len(array)-1)
    return array[num]

arson = [2, 3, 2, 5, 8, 1, 9, 8, -7, 8, -15, -15]
print(rand_elem(arson), end=" ")
print(rand_elem(arson), end=" ")
print(rand_elem(arson), end=" ")
print(rand_elem(arson), end=" ")