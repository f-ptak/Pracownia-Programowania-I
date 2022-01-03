difrray = [5,1,9,6,1]

print("Array:", difrray)

i = 0
maxnum = difrray[0]
while i < len(difrray):
    if difrray[i] > maxnum:
        maxnum = difrray[i]
    i+=1

i = 0
minnum = difrray[0]
while i < len(difrray):
    if difrray[i] < minnum:
        minnum = difrray[i]
    i+=1


difference = maxnum - minnum

print("Result:", difference)