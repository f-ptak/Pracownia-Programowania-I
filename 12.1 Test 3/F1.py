class C():
    def __init__(self, calk):
        self.calk = calk
        
    def __str__(self):
        if self.calk > 0:
            return self.calk*"*"
        else:
            return ""