def f5(c,n):
    with open("9.1.5 beautybeast.txt") as file:
        for i in range(n):
            line = file.readline()
        
    return (c in line)

print(  f5("s",3)  )
print(  f5("o",22)  )
print(  f5("1",11)  )
print(  f5("A",30)  )