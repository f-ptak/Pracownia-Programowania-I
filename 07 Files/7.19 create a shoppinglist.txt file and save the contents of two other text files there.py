with open("7.19 MeatAndFish.txt") as meat, open("7.19 GrainsAndBread.txt") as bread, open("7.19 shoppinglist.txt", "w") as shoplist:
    meatlist = meat.read()
    breadlist = bread.read()
    shoplist.write(meatlist+"\n"+breadlist)