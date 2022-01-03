import re

with open("7.13 Stardust Pipeline.txt", encoding="utf_8") as file:
    readfile = file.read()
    wordlist = re.findall(r"\w\w\w\w\w\w+", readfile)
    
    print(wordlist)