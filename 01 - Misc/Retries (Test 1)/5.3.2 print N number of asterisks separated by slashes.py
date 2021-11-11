def asterisks_slashes(n):
    streeng = ''
    last = ('*')
    if n == 1:
        return last
    else:
        for i in range(n-1):
            streeng += '*/'
        return streeng + last


print(asterisks_slashes(7))