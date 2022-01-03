def rand_elem(ranray):
    import random
    counter = random.randint(0,len(ranray)-1)
    elem = ranray[counter]
    
    return elem


ogray = [4,1,77,5,2,-9,8,15,7,64,423,9,5,0,39]
print("Random array element: ", rand_elem(ogray))