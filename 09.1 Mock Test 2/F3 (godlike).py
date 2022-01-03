import re

def f3(t):
    numbers = re.findall("[0-9]+", t)
    counter = 0
    for i in numbers:
        if (int(i) <= -10 or int(i) >= 10) and (int(i) > -1000 and int(i) < 1000):
            counter += int(i)
    return counter

print(f3("198fan s372*39338s s10j9f"))
print(f3("Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"))