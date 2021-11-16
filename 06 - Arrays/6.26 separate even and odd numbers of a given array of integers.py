oddray = [4,2,5,13,8,4,7,9,5,15,523,34,65,75,23,-123,18,-42,67,56,5,54,16,76,0]

i = 0
while i < len(oddray):
    j = 0
    while j < len(oddray):
        if (oddray[i] % 2) == 0:
            temp = oddray[i]
            del oddray[i]
            oddray.insert(0,temp)
        else:
            temp = oddray[i]
            del oddray[i]
            oddray.insert(len(oddray),temp)
        j+=1
    i+=1

print("Evens first, odds second:", oddray)