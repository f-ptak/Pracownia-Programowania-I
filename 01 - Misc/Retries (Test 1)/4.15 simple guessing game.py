def read_number():
    num = int(input("Enter a number from 1 to 9: "))
    return num
    
def generate_number():
    import random
    pc_num = random.randint(1,9)
    return pc_num
    
def play_game():
    user = read_number()
    pc = generate_number()
    
    if user == pc:
        print("You win!")
    else:
        print("You lost...")


play_game()