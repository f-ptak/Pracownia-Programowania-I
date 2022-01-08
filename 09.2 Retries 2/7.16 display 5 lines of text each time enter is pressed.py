with open("7.13 Stardust Pipeline.txt", encoding="utf8") as file:
    length = 5
    for i in range(length):
        print(file.readline(), end="")
    
    while True:
        print("======================================")
        key = input("To display 5 next lines press Enter:\n======================================")
        
        if key == "":
            for i in range(length):
                print(file.readline(), end="")
        else:
            break
    
        if file.readline() == "":
            break