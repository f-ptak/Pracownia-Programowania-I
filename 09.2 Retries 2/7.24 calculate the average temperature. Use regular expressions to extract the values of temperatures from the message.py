import re

txt = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

pattern = "\d{2}"
temperatures = re.findall(pattern, txt)

sumson = 0
for temp in temperatures:
    sumson += int(temp)

print(sumson/len(temperatures))