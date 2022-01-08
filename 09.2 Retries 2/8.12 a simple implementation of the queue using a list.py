queue = []

def push(value):
    queue.append(value)

def pop():
    if not empty():
        return queue.remove(queue[0])
    else:
        return None

def empty():
    return queue == []

def display():
    for value in queue:
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