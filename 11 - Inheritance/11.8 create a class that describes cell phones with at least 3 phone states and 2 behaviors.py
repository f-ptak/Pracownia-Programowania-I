class Phone():
    def __init__(self, name, brand, RAM, size):
        self.name = name
        self.brand = brand
        self.RAM = RAM
        self.size = size
        self.on = True
    
    def __str__(self):
        return str("| "+ self.name + " | Made By: " + self.brand + " | " + str(self.RAM)
                   + "GB RAM | " + str(self.size) + " Inch Screen" + " | Turned on? " + str(self.on))
    
    def onoff(self):
        if self.on:
            self.on = False
        else:
            self.on = True
    
    def addRAM(self):
        self.RAM += int(input("Get more RAM: "))

rinukusu = Phone("Sabsonu 6", "Dooru", 4, 5.9)
ajbonu = Phone("Ajbonu 15 Puro Eksu Purasu Layto", "Frooto", 1, 6.8)

print(rinukusu)
rinukusu.onoff()
print(rinukusu)

print(ajbonu)
ajbonu.addRAM()
ajbonu.onoff()
print(ajbonu)