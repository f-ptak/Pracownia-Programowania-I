def count_coins():
    value = int(input('Enter value: '))
    
    five = value // 5
    two = (value % 5) // 2
    one = (value % 5) % 2
    
    summ = five+two+one
    
    print(f'there are {summ} coins in total\n{five} fives, {two} twos, {one} ones')


count_coins()