with open("7.22 number powers.txt", "w") as powers:
    for i in range(1,11):
        powers.write(f"{str(i)},{str(i**2)},{str(i**3)}\n")