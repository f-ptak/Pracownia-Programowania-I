def randray(array):
    import random
    num = random.randint(0,len(array))
    value = array[num]
    return value

hugeray = []
for i in range(1,1000):
    hugeray.append(i)

randum = randray(hugeray)
length = 8

print("-",end="")
print("-----"*length)
print("|", end="")
for l in range(length):
    print(f" {randray(hugeray):3d}|", end="")
print()
print("-",end="")
print("-----"*length)