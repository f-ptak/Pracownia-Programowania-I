def coins(price):
    five = price // 5
    two = (price % 5) // 2
    one = (price % 5) % 2
    print(five+two+one)