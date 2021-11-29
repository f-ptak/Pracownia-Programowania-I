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
        if c=="(":
            push(c)
        elif c==")":
            while stack[-1] != "(":
                result.append(stack[-1])
                del stack[-1]
            del stack[-1]
        elif c=="*" or c=="/":
            push(c) 
        elif c=="+" or c=="-":
            counter = 0
            counter += stack.count("*")
            counter += stack.count("/")
            if counter != 0:
                while not empty() and stack[-1] != "(":
                    result.append(stack[-1])
                    del stack[-1]
            push(c)
        elif c=="=":
            while not empty():
                result.append(stack[-1])
                pop()
            result.append("=")
            return result
        else:
            push(c)
            result.append(stack[-1])
            del stack[-1]

inputexp = list(input("Enter an expression: "))
# inputexp = list("8 / (3 + 1) * (3 - 2 + 4) = ")

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