def max4(n1,n2,n3,n4):
    nums = (n1,n2,n3,n4)
    maxnum = n1
    for i in range(len(nums)):
        if nums[i] >= maxnum:
            maxnum = nums[i] 
    return maxnum


print(max4(4234,234525345,32,345345))