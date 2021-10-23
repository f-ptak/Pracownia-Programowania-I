human = int(input('Enter the dog\'s age in human years: '))

if human <= 2:
    dog = human * 10.5
else:
    dog = 21 + (human-2)*4

print(f'The dog\'s age in dog’s years is {dog} years.')