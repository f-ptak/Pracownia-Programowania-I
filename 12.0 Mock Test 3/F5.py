class C():
    def __init__(self, t):
        self.t = t
    
    def m1(self):
        fulldic = {}
        
        for i in range(len(self.t)):
            if self.t[i] not in fulldic:
                fulldic[self.t[i]] = 1
            else:
                fulldic[self.t[i]] += 1
                
        return fulldic
    
    def m2(self,let):
        seldic = {}
        
        for i in range(len(let)):
            if let[i] not in seldic:
                seldic[let[i]] = 0
        
        for i in range(len(self.t)):
            if self.t[i] in seldic:
                seldic[self.t[i]] += 1
        
        return seldic


print(C("my moon").m1())
print(C("my moon").m2("mn"))