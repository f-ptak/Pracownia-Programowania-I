def display_text():
    five = ""
    for line2 in range(5):
        five += file.readline()
    return five

with open("7.13 Stardust Pipeline.txt", "r", encoding="utf_8") as file:
    counter = 0
    for line in file:
        counter+=1
    file.seek(0,0)
    
    print(display_text())
    
    ren = 0
    while (ren < counter-5) and input("Press Enter to proceed...\n") == "":
        ren+=5
        print(display_text())