with open("7.20 numbers.txt", "w") as numbers:
    text = ""
    for i in range(1,51):
        text += str(i)
        text += "\n"
    numbers.write(text)