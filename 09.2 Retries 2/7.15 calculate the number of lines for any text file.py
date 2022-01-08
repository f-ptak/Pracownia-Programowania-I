with open("7.13 Stardust Pipeline.txt", encoding="utf8") as file:
    count = 0
    for line in file:
        count += 1
    
    print(f"filename: \"{file.name}\"")
    print("Number of lines:", count)