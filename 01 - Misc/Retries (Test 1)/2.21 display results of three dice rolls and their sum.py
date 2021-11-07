def disp_dice():
    import random
    one = 0
    two = 0
    three = 0
    num = (one,two,three)
    numlist = list(num)
    for i in range(0,3):
        numlist[i] = random.randrange(1,7)
    summ = sum(numlist)
    
    print(f'dice number one: {numlist[0]}\ndice number two: {numlist[1]}\ndice number three: {numlist[2]}')
    print(f'their sum: {summ}')
    
disp_dice()