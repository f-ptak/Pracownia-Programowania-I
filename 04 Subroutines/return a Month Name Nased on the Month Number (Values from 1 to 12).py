def month(n):
    if n<1 or n>12:
        print('No such month')
        exit()
    elif n == 1:
         n = 'January'
    elif n == 2:
         n = 'February'
    elif n == 3:
         n = 'March'
    elif n == 4:
         n = 'April'
    elif n == 5:
         n = 'May'
    elif n == 6:
         n = 'June'
    elif n == 7:
         n = 'July'
    elif n == 8:
         n = 'August'
    elif n == 9:
         n = 'September'
    elif n == 10:
         n = 'October'
    elif n == 11:
         n = 'November'
    elif n == 12:
         n = 'December'
    return n

x = int(input('Choose a month: '))
month(x)
print(f'{x} month is {month(x)}')