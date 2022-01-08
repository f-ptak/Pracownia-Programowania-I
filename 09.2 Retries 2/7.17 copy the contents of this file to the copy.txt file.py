with open("7.13 Stardust Pipeline.txt", encoding="utf8") as file:
    content = file.read()
    
    with open("7.17 copy.txt", "w", encoding="utf8") as copy:
        copy.write(content)