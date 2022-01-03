def return_fib(n):
    younger = 0
    older = 1
    fib = 0

    for i in range(1,n):
        fib = younger + older
        younger = older
        older = fib
    
    print()
    return younger


print(return_fib(5))