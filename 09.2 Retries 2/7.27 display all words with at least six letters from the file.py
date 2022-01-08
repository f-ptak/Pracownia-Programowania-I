import re

with open("7.13 Stardust Pipeline.txt", encoding="utf8") as file:
    content = file.read()

pattern = "[a-zA-Z]{6}[a-zA-Z]*"
# pattern = "\w{6}\w*"

sixes = re.findall(pattern, content)

for word in sixes:
    print(word)