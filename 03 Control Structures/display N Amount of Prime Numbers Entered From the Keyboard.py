N = int(input('Enter amount: '))
i = 0
prime = 2
while i<N:
    for j in range(2,int(prime/2)+1):
        if (prime % j) == 0:
            break
    else:
        print(f'{prime} ', end='')
        i+=1
    prime+=1