with open("7.12 shopping.txt", "a") as file:
    while True:
        product = input("Enter name of a product\n(stop adding products with '0'): ")
        if product != "0":
            file.write(f"{product}\n")
        else:
            break