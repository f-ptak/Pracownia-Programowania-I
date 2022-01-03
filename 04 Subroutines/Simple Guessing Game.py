import mymath

me = mymath.read_number()
pc = mymath.generate_number()

if me == pc:
    print('You win!')
    print(pc)
else:
    print('You lost...')
    print(pc)