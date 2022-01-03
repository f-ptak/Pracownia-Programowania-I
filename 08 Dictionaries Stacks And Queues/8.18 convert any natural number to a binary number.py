stack = []

def push(value):
    stack.append(value)

def convert_tobin(deci):
    if deci != 0:
        push(deci % 2)
        convert_tobin(deci//2)

def display_binnum(numindec):
    convert_tobin(numindec)
    
    binnum = ""
    for i in range(len(stack)):
        binnum += str(stack.pop())
    return binnum

december = int(input("Enter a natural number in decimal number system: "))

print(f"Natural number: {december}\nBinary number: {display_binnum(december)}")