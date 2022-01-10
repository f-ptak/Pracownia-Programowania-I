class C():
    def __init__(self, t):
        self.t = t
    
    def m(self):
        counter = 0
        
        for i in range(len(self.t)-2):
            if self.t[i] == self.t[i+2] and self.t[i+1] != self.t[i]:
                counter += 1
        return counter

print(C([True,False,False]).m())
print(C([True,False,True,False]).m())
print(C([True,False,True,True,False,True,False,True,False]).m())