class C():
    def __init__(self, names):
        self.names = names
    
    def m(self):
        nameray = []
        for name in self.names:
            nameray.append(name.upper())
        
        for i in range(len(nameray)):
            counter = nameray.count(nameray[i])
            if counter > 1:
                return True
        return False
            
        

print(C(["Anna"]).m())
print(C(["Anna","John"]).m())
print(C(["Anna","John","Anna"]).m())
print(C(["ANNA","John","Anna"]).m())