import re

text = "To be, or not to be, that is the question"

pattern = "[aeiou]"
vowels = re.findall(pattern, text)

print(len(vowels))