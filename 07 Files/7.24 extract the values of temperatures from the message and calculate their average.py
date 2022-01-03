import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatures = re.findall("\d{2}",message)

tempsum = 0
for i in temperatures:
    tempsum += int(i)

print(tempsum/len(temperatures))