def input_num():
    num = int(input('Enter a number from 1 to 6: '))
    if num < 1 or num > 6:
        print('Wrong number, try again.')
        input_num()
    else:
        return num


def ask_again():
    again = int(input('Would you like to try again?\n1. YES \n2. NO\n'))
    if again == 1:
        guess_num()
    elif again == 2:
        print('See you soon!')
    else:
        print('Wrong option, try again.')
        ask_again()


def guess_num():
    import random
    
    user = input_num()
    pc = random.randint(1,6)
    
    print(f'PC\'s number is {pc}, your number is {user}')
    if pc == user:

        print(f'YOU WIN!')
    else:
        print(f'YOU LOST...')
    
    ask_again()


guess_num()