# tip x^n = x * x^(n-1)
# 5^2 --> 5*5    5^3 --> 5*5*5

def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        value = x
        for i in range(1,n):
            value *= x
        return value
    else:
        n = n * -1
        value = x
        for i in range(1,n):
            value *= x
        result = 1/value
        return result

base = int(input('Enter the base: '))
exponent = int(input('Enter the exponent: '))
print(f'The value of {base} to the power of {exponent} is', power(base, exponent))