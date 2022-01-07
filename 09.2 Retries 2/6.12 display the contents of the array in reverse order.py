arson = [15, 8, 31, 47, 2, 19]

print("original array:", end=" ")
for i in arson:
    print(i, end=" ")

print("\nreversed array:", end=" ")
for i in range(len(arson),0,-1):
    print(arson[i-1], end=" ")

print("\nreversed array (method 2):", end=" ")
for i in arson[::-1]:
    print(i, end=" ")