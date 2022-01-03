colors = ["red","orange","blue","green","yellow","purple","brown"]

file = open("6.15 colors.txt", "a")

for i in range(0,len(colors)):
    file.write(f"{colors[i]}\n")


file.close()