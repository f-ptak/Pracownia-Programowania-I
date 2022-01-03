def calculate_sum(n):
    if n==0:
        return 0
#    if n==1:
#        return 1
    if n >= 1:
        return n + calculate_sum(n-1)

N = int(input('Enter a number: '))
print( f"sum of all natural numbers between 1 and {N} is {calculate_sum(N)}" )
