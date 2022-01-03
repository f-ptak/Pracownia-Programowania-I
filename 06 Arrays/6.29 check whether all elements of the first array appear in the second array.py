firay = [-7, 3, 5, 9, 1]
secray = [2, 3, 2, 5, 8, 1, 9, 8, -7, 8, -15, -15]

print("First array:", end=" ")
for p in range(len(firay)):
    print(firay[p], end=" ")
print("\nSecond array:", end=" ")
for p in range(len(secray)):
    print(secray[p], end=" ")

for m in range(len(firay)): 
    for n in range(len(secray)):
        if firay[0] == secray[n]:
            del firay[0]
            break

print("""
""")
if firay == []:
    print("First array is a subset of the second array")
else:
    print("First array is not a subset of the second array")