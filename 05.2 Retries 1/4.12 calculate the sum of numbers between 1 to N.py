def summ(N):
    if N==1:
        return 1
    if N>1:
        return N + summ(N-1)


x = int(input("Enter a number: "))
print(summ(x))