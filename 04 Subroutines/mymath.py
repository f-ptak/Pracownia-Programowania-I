def read_number():
    input_number = int(input('Enter a number from 1 to 9: '))
    if 0 < input_number < 10:
        return input_number
    else:
        return read_number()

def generate_number():
    import random
    random_number = random.randrange(1,10)
    return random_number