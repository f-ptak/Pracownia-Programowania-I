def return_prime(n):
    prime = 2
    counter = 0
    
    while counter < n:
        for i in range(2,prime):
            if prime % i == 0:
                break
        else:
            counter+=1
        prime+=1
    
    return prime-1


print(return_prime(25))