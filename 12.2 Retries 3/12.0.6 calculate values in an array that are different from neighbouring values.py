class C():
    def __init__(self, arson):
        self.arson = arson
    
    def m(self):
        counter = 0
        for i in range(len(self.arson)-2):
            if self.arson[i+1] != self.arson[i] and self.arson[i+1] != self.arson[i+2]:
                counter += 1
                
        return counter

print(C([True,False,False]).m())
print(C([True,False,True,False]).m())
print(C([True,False,True,True,False,True,False,True,False]).m())