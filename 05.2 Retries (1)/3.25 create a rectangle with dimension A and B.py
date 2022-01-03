def create_rectangle():
    a = int(input("Enter the lenght of side A: "))
    b = int(input("Enter the lenght of side B: "))
    
    print(b*"*")
    for i in range(0,a-2): 
        print(f'*{(b-2)*" "}*')
    print(b*"*")


create_rectangle()