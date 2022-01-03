def disp_pad_for():
    print("FOR LOOP")
    for i in range(1,8,3):
        for j in range(0,3):
            print(i+j, end=" ")
        print()

def disp_pad_while():
    print("WHILE LOOP")
    x = 1
    while x < 8:
        y = 0
        while y < 3:
            print(x+y, end=" ")
            y += 1
        x += 3
        print()    


disp_pad_for()
disp_pad_while()