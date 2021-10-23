amount = int(input('Enter the amount in PLN: '))

pięć = amount // 5
dwa = (amount % 5) // 2
jeden = ((amount % 5) % 2) // 1

print(f'The amount of PLN {amount} in coins: \n5 zł - {pięć} \n2 zł - {dwa} \n1 zł - {jeden}')