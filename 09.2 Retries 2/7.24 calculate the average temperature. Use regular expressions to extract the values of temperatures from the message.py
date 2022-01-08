import re

txt = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

pattern = "\d{2}"
temperatures = re.findall(pattern, txt)

average = 0
for temp in temperatures:
    average += int(temp)/3

print(average)