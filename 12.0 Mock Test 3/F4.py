class C():
    def __init__(self,numdic):
        self.numdic = numdic
    
    def m(self):
        vallist = list(self.numdic["value"])
        for i in range(len(vallist)):
            vallist[i] = int(vallist[i])
        sysnum = int(self.numdic["system"])
        
        for i in range(len(vallist)):
            if vallist[i] >= sysnum:
                return -1
        
        dec = 0
        for i in range(len(vallist)):
            dec += vallist[-1-i] * (sysnum**i)
        return dec

print(C({"system":"2", "value":"101"}).m())
print(C({"system":"8", "value":"70281"}).m())

print(C({"system":"2", "value":"101001"}).m())
print(C({"system":"3", "value":"211"}).m())
print(C({"system":"8", "value":"21"}).m())