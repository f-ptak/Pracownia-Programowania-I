colarson = ["blue","orange","yellow","green","purple","red"]

with open("6.15 colors.txt", "a") as colors:
    for i in colarson:
        colors.write(f"{i}\n")