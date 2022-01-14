class C():
    def __init__(self, arson):
        self.arson = arson
    
    def m(self):
        for num in self.arson:
            if self.arson.count(num) > 1:
                return True
        return False