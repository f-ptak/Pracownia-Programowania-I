print('for:')
for i in range(6,-1,-3):
    for j in range(1,4):
        print(f' {i+j}',end='')
    print()

print('\none while:')
x = 6
while x>-1:
    for y in range(1,4):
        print(f' {x+y}',end='')
    x-=3
    print()

print('\ntwo whiles:')
m = 6
while m>-1:
    n=1
    while n<4:
        print(f' {m+n}',end='')
        n+=1
    print()
    m-=3