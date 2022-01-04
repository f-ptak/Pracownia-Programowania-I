class C():
    def __init__(self,text):
        self.text = text
    
    def m(self):
#         counter = 0
#         textray = list(self.text)
#         for i in range(len(textray)):
#             for j in range(len(textray)):
#                 if textray[j] == textray[i]:
#                     counter += 1
#             if counter > len(textray):
#                 return False
#         return True

        textray = list(self.text)
        for i in range(len(textray)):
            counter = textray.count(textray[i])
            if counter > 1:
                return False
        return True

print(C("red sun").m())
print(C("blue water").m())
print(C("BLUE water").m())