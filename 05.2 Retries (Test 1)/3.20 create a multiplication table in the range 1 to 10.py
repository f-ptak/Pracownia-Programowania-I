def input_number():
    number = int(input("Enter a number from 1 to 10: "))
    if number < 1 or number > 10:
        print('Wrong number, try again.')
        input_number()
    else:
        return number

def create_table():
    num = input_number()
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
    
create_table()