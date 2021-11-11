def return_sum(n):
    nlist = list(str(n))
    intnlist = map(int,nlist)
    value = sum(intnlist)
    return value


print(return_sum(81))