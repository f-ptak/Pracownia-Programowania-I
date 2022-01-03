# ogray = [1,2,3,4,5,6,7,8,9]
ogray = [1,234,344,34,545,32,15,0,-123,43,55,2,5,1,7,4,54,16,-111,-23,43,67,73]

ogray = list(map(float, ogray))

# ogray = [float(i) for i in ogray]

# for i in range(len(ogray)):
#     ogray[i] = float(ogray[i])

num = float(input("Enter a real number: "))

i = 0
while i < len(ogray):
    if ogray[i] < num+1:
        del ogray[i]
        i-=1
    i+=1


print("bigger numbers in the array are:", end=" ")
for p in range(len(ogray)):
    print(ogray[p], end=" ")