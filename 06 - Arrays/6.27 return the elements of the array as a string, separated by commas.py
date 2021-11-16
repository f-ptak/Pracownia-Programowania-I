def streeng(intray):
    strray = ""
    i = 0
    while i < len(intray):
        strray += str(intray[i])
        if i < len(intray)-1:
            strray += ", "
        i+=1

    return strray

ogray = [5,4,3,2,6,5]
print("Array:", ogray)
print("String: ", streeng(ogray))