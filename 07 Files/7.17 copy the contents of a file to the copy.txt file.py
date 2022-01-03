with open("7.13 Stardust Pipeline.txt", "r", encoding="utf_8") as original:
    text = original.read()

with open("7.17 text file copy.txt", "w", encoding="utf_8") as copy:
    copy.write(text)