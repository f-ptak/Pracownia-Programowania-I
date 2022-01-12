class C():
    def __init__(self, text):
        self.text = text
    
    def m(self):
        for char in self.text:
            if self.text.count(char) > 1:
                return False
        return True

print(C("red sun").m())
print(C("blue water").m())
print(C("BLUE water").m())