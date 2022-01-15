class C():
    def __init__(self, arson):
        self.arson = arson
    
    def m(self):
        checkson = []
        for i in range(len(self.arson)-2):
            onetwo = self.arson[i+1] - self.arson[i]
            twothree = self.arson[i+2] - self.arson[i+1]
            
            if onetwo == twothree:
                checkson.append(onetwo)
            else:
                return -1
            
        return len(checkson)+1