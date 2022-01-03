amount = int(input("How many prime numbers to display: "))
prime = 2
i = 0
while i < amount:
    for j in range(2, prime):
        if prime%j == 0:
            break
    else:
        print(prime, end=" ")
        i += 1
    prime += 1