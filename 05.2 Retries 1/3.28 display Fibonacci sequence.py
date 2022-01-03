# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

def disp_fibonacci():
    m = 0
    n = 1
    o = 0
    i = 0
    while i < 50:
        print(m, end=" ")
        o = m + n
        m = n
        n = o
        i += 1


disp_fibonacci()