with open("7.13 Stardust Pipeline.txt", "r", encoding="utf_8") as original:
    with open("7.18 copylines.txt", "w", encoding="utf_8") as copy:
        for line in original:
            copy.write(line)