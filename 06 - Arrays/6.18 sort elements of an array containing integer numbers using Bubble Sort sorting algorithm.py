def bubblesort(arr):
    
    j=0
    while j < len(arr)-1:
        i=0
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                temparr = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temparr
            i+=1
        j+=1
    
    return arr


testarr0 = [3,2,1,0]
testarr1 = [9,8,7,6,5,4,3,2,1]
testarr2 = [1,67,423,2,4,7,13,5]
testarr3 = [4,254,2,3,553,123,13,4,5,5]
print(bubblesort(testarr0))
print(bubblesort(testarr1))
print(bubblesort(testarr2))
print(bubblesort(testarr3))