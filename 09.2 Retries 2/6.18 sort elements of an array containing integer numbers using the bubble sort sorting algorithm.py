def bubblesort(arson):
    for j in range(len(arson)):
        for i in range(len(arson)-1):
            temp = []
            if arson[i] > arson[i+1]:
                temp = arson[i]
                arson[i] = arson[i+1]
                arson[i+1] = temp
    
    return arson


testarr0 = [3,2,1,0]
testarr1 = [9,8,7,6,5,4,3,2,1]
testarr2 = [1,67,423,2,4,7,13,5]
testarr3 = [4,254,2,3,553,123,13,4,5,5]
print(bubblesort(testarr0))
print(bubblesort(testarr1))
print(bubblesort(testarr2))
print(bubblesort(testarr3))
print(bubblesort([17,13,8,3,14,25,15,16,-11]))