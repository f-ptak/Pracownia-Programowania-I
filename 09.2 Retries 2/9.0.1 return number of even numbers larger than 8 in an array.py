def f1(arson):
    counter = 0
    for val in arson:
        if val%2 == 0 and val > 8:
            counter += 1
    return counter

print(f1([13,7,4,16,3,12,8]))