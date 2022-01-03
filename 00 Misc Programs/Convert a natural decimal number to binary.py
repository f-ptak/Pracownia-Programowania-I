def NATtoBIN(IN, OP):
    if IN <= 0:
        STROP = ""
        for i in range(len(OP),0,-1):
            STROP += str(OP[i-1])
        STROP += "\n"
        
        OP = OP[::-1]
        for num in OP:
            STROP += str(num)
        return STROP
    else:
        DIG = IN % 2
        OP += str(DIG)
        return NATtoBIN(IN//2, OP)

# NAT = int(input("wprowadz liczbe NATowita: "))
NAT = 41
#      101001
BIN = []

result = NATtoBIN(NAT, BIN)
print(result)