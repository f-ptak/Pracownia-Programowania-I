def inrange(n,start,end):
    if start >= end:
        print("Wrong range")
        quit()
    else:
        if n >= start and n <= end:
            return True
        else:
            return False
    
    
    
x = int(input("Enter a number: "))
first = int(input("Enter start of the range: "))
last = int(input("Enter end of the range: "))

print("\nIs the number within the given range?")
print(inrange(x,first,last))