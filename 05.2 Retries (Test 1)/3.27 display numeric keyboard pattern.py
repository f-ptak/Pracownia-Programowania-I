def for_pattern():
    print("FOR PATTERN")
    for i in range(6,-1,-3):
        for j in range(1,4):
            print(f' {i+j}',end='')
        print()

def while_pattern():
    print("WHILE PATTERN")
    i = 7
    while i > 0:
        j = 0
        while j < 3:
            print(i+j, end=" ")
            j+=1
        i-=3
        print()


for_pattern()
while_pattern()