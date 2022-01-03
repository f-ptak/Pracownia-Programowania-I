import re

text = "To be, or not to be, that is the question"
print(len(re.findall("a|e|i|o|u",text)))