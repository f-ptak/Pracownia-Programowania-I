class C():
    def __init__(self, t):
        self.t = t
    
    def m1(self):
        dic = {}
        
        for i in range(len(self.t)):
            if self.t[i] not in dic:
                dic[self.t[i]] = 1
            else:
                dic[self.t[i]] += 1
            
        return dic
    
    def m2(self, c1):
        dic = {}
        
        for i in range(len(c1)):
            if c1[i] not in dic:
                dic[c1[i]] = 0
        
        for i in range(len(self.t)):
            if self.t[i] in dic:
                dic[self.t[i]] += 1
        
        return dic

print(C("my moon").m1())
print(C("my moon").m2("mn"))