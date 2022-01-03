def disp_lot():
    i=1
    while i < 8:
        j = i
        while j < 50:
            print(j, end=" ")
            j += 7
        print()
        i += 1


disp_lot()