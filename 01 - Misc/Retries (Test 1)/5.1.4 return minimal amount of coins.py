def coins(price):
    five = price // 5
    two = (price % 5) // 2
    one = (price % 5) % 2
    return five+two+one


x = int(input("Enter a price: "))
print(coins(x))