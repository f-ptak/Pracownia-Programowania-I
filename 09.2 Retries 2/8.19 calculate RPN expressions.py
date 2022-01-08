stack = []

def push(value):
    stack.append(value)

def pop():
    if len(stack) != 0:
        return stack.pop()
    else:
        return None

exp = input("Enter an expression: ")

signs = ["+","-","*","/"]
for val in exp:
    if val == " ":
        continue
    try:
        push(int(val))
    except:
        if val in signs:
            one = pop()
            two = pop()
            
            if val == "+":
                push(two + one)
            elif val == "-":
                push(two - one)
            elif val == "*":
                push(two * one)
            elif val == "/":
                push(two / one)
        
        elif val == "=":
            three = stack[-1]
            stack.pop()
            print("Result:", three)