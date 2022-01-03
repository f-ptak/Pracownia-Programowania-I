def return_sequence(n):
    i = 1
    streeng = ''
    while i <= n:
        streeng += str(i)
        i+=1
    return streeng


print(return_sequence(11))