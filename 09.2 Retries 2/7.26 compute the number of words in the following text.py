import re

text = "To be, or not to be, that is the question"

pattern = "[a-zA-Z]+"

words = re.findall(pattern, text)

print(len(words))