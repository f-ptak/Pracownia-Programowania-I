with open("7.19 MeatAndFish.txt") as meat, open("7.19 GrainsAndBread.txt") as bread:
    meatent = meat.read()
    breadent = bread.read()
    
    with open("7.19 shopping list.txt", "w") as shop:
        shop.write(f"{meatent}\n{breadent}")