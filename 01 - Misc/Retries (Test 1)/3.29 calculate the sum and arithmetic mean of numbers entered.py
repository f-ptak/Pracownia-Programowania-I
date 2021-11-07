def calc_entered():
    quantity = 0
    summ = 0
    mean = 0
    value = int(input("Enter a number: "))
    
    while value != 0:
        quantity += 1
        summ += value
        mean = summ / quantity
        value = int(input("Enter a number: "))
    
    print(f"Quantity={quantity}, Sum={summ}, Mean={mean}")   


calc_entered()