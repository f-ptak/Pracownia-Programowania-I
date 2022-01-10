class C():
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def __str__(self):
        namelist = list(self.name)
        surlist = list(self.surname)
        return (namelist[0] + surlist[0]).upper()

print(C("anna","may"))