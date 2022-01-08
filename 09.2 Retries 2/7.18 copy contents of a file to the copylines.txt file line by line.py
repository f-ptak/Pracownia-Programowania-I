with open("7.13 Stardust Pipeline.txt", encoding="utf8") as file:
    content = file.read()
    
    with open("7.18 copylines.txt", "w", encoding="utf8") as copy:
        for line in content:
            copy.write(line)