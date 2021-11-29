stack = []
def push(value):
    stack.append(value)
def pop():
    if not empty():
        return stack.pop()
    else:
        return None
def empty():
    return len(stack) == 0
def display():
    for val in stack:
        print(val, end=" ")
    print()

def clean_input(dirtyexp):
    e = 0
    while e < len(dirtyexp):
        if dirtyexp[e] == " ":
            del dirtyexp[e]
            e -= 1
        e += 1
    for d in range(len(dirtyexp)):
        try:
            dirtyexp[d] = int(dirtyexp[d])
        except:
            continue
    return dirtyexp

def calc_rpn(calcexp):
    result = []
    for c in calcexp:
        if c=="+" or c=="-" or c=="*" or c=="/":
            if not empty():
                result.append(stack[-1])
            pop()
            if not empty():
                result.append(stack[-1])
            pop()
            push(c)
        elif c == "=":
            while not empty():
                result.append(stack[-1])
                pop()
            result.append("=")
            
            b = 0
            while b < len(result):
                if result[b] == "(" or result[b] == ")":
                    del result[b]
                    b -= 1
                b += 1
            return result
        else:
            push(c)

inputexp = list(input("Enter an expression: "))

print("Input Exp: ", end=" ")
for p in range(len(inputexp)):
    print(inputexp[p], end=" ")

cleanexp = clean_input(inputexp)

print()
print("Clean Exp: ", end=" ")
for p in range(len(cleanexp)):
    print(cleanexp[p], end=" ")
print()

print("Result Exp:", end =" ")
resultexp = calc_rpn(cleanexp)
for p in range(len(resultexp)):
    print(resultexp[p], end=" ")
print()