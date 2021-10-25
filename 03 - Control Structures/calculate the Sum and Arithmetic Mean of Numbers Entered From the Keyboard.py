number = int(input('Enter number: '))
quantity = 0
prev_summ = 0
summ = 0
mean = 0
while number !=0:
    quantity += 1
    summ = number + prev_summ
    prev_summ = summ
    mean = summ/quantity
    number = int(input('Enter number: '))
print(f'Quantity = {quantity}, Sum = {summ}, Mean = {mean}')