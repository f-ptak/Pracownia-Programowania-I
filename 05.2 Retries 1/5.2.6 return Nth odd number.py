def return_odd(x,n):
    odd = 1
    counter = 0
    
    while counter < n:
        if odd % 2 == 0:
            pass
        else:
#            print(odd, end=" ")
            counter+=1
        odd+=x
        
    return odd-x


print(return_odd(2,8))
print(return_odd(3,4))

print(return_odd(3,12))