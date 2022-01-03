def minmax(n1,n2,n3):
    nums = (n1,n2,n3)
    minnum = n1
    maxnum = n1
    for i in range (len(nums)):
        if nums[i] >= maxnum:
            maxnum = nums[i]
    
    for i in range (len(nums)):
        if nums[i] <= minnum:
            minnum = nums[i]
            
    return maxnum - minnum


print(minmax(15,10,25))