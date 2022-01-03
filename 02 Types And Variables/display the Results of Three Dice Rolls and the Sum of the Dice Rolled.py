import random

one = random.randrange(1,6)
two = random.randrange(1,6)
three = random.randrange(1,6)
print('diceroll one: {}\ndiceroll two: {}\ndiceroll three: {}'.format(one, two, three))

sum = one + two + three
print('sum of the dice rolled: ', sum)