powers = [8,2,5,1,9]
secondpowers = powers.copy()

for i in range(0,len(powers)):
    secondpowers[i]= powers[i]**2


print("array: ", end="")
for p in range(0,len(powers)):
    print(powers[p], end=" ")
    
print("\nsecond power: ", end="")
for p in range(0,len(powers)):
    print(secondpowers[p], end=" ")