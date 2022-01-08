stack = []

natu = 18

temp = natu
while True:
    if temp != 0:
        stack.append( (temp%2) )
        temp = temp // 2
    else:
        break

bina = ""
lengson = len(stack)
for i in range(lengson):
    bina += str(stack[-1])
    stack.pop()

print("Natural number:", natu)
print("Binary number:", bina)