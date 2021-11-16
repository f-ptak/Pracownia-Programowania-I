numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
numberswhile = numbers.copy()
numbersfor = numbers.copy()
# numberswhile = [15, 8, 31, 47, 2, 19]

print("array: ", end="")
for x in range(0,len(numbers)):
    print(numbers[x], end=" ")

for i in range (0,len(numberswhile)//2):
    tenp = numberswhile[i]
    numberswhile[i] = numberswhile[len(numberswhile)-1-i]
    numberswhile[len(numberswhile)-1-i] = tenp

print("\nreversed array using for loop: ", end="")
for x in range(0,len(numbers)):
    print(numberswhile[x], end=" ")

# =============================================

j = len(numbersfor) - 1
i = 0
while(i < j):
    temp = numbersfor[i]
    numbersfor[i] = numbersfor[j]
    numbersfor[j] = temp
    i += 1
    j -= 1 
print("\nreversed array using while loop: ", end="")
for x in range(0,len(numbers)):
    print(numbersfor[x], end=" ")
# =============================================