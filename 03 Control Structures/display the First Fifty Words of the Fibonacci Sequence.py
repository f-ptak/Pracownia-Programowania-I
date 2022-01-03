i=0
M=0
N=1
F=0
print(M, N, end=' ')
while i<47:
    F=M+N
    print(f'{F} ', end='')
    M=N
    N=F
    i+=1
print('...')