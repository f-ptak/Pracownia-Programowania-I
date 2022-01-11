class Thermometer():
    def __init__(self):
        self.ison = False
    
    def onoff(self):
        if self.ison:
            self.ison = False
        else:
            self.ison = True
    
    def measure(self):
        if self.ison:
            import random
            self.temp = round(random.uniform(34,42), 1)

        else:
            print("Thermometer isn't turned on!")
    
    def display(self):
        if self.ison:
            message = f"Temperature: {self.temp}C"
            if self.temp >= 37:
                message += " (fever)"
            if self.temp >= 41:
                message += " CRITICAL TEMPERATURE!!"
            
            print(message)
            
        else:
            print("Thermometer isn't turned on!")
        

t = Thermometer()

t.measure()
t.onoff()
t.measure()
t.display()
t.measure()
t.display()
t.measure()
t.display()
t.measure()
t.display()
t.onoff()
t.display()