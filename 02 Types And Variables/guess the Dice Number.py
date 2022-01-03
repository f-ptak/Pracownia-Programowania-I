import random

number = random.randrange(1,6)

print('enter your guess: ')
s_guess = input()
guess = int(s_guess)

print(number == guess)