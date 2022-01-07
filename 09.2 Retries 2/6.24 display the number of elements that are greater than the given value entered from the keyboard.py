arson = [6,8,3,1,0,5,7]
num = float(input("Enter a real number: "))

counter = 0
for pos in arson:
    if pos > num:
        counter += 1

print(counter)