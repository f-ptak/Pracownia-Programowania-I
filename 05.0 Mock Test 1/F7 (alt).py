def bonus(years):
    i = 1
    b = 0
    while(i <= years):
        if i <= 5:
            b += 100
        elif i > 5 and i <=8:
            b += 200
        else:
            b += 50
        i += 1
    print(b)