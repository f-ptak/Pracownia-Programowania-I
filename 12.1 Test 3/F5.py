class C():
    def __init__(self, arson):
        self.arson = arson
    
    def m(self):
        for i in range(0,len(self.arson),2):
            if self.arson[i] % 2 != 0:
                return False
        
        for i in range(1,len(self.arson),2):
            if self.arson[i] % 2 == 0:
                return False
        
        return True