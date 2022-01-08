with open("7.09 numbers.txt") as file:
    sumson = 0
    for line in file:
        sumson += int(line)
    
    print(sumson)