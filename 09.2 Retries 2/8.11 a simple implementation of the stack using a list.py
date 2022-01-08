stack = []

def push(value):
    stack.append(value)

def pop():
    if not empty():
        stack.pop()

def empty():
    return stack == []

def display():
    for value in stack:
        print(value, end=" ")
    print()

display()
push(2)
push(14)
push(9)
display()
pop()
display()
push(31)
push(6)
display()
pop()
pop()
display()