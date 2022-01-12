class C():
    def __init__(self, arson):
        self.arson = arson
    
    def m(self):
        for i in range(len(self.arson)):
            self.arson[i] = self.arson[i].lower()
        
        for name in self.arson:
            if self.arson.count(name) > 1:
                return True
        return False

print(C(["Anna"]).m())
print(C(["Anna","John"]).m())
print(C(["Anna","John","Anna"]).m())
print(C(["ANNA","John","Anna"]).m())