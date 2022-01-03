print('enter the amount of PLN: ')
s_Amount = input()
Amount = float(s_Amount)

VAT = 0.23*Amount

result= 'Amount  : {:>10,.2f} zł \nVAT 23% : {:>10,.2f} zł'
print(result.format(Amount, VAT))