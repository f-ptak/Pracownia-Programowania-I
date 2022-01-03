class Termometer():
    import random
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    
    def measure(self):
        self.temp = round(self.random.uniform(34,42),1)
    
    def disp_temp(self):
        try:
            print(f"Measured temperature: {self.temp}C", end="")
            if self.temp >= 37:
                print(" (fever)", end="")
            if self.temp >= 41:
                print(" CRITICAL TEMPERATURE!!", end="")
            print()
        except AttributeError:
            print("No temperature measured")
            pass

term = Termometer()

term.turn_on()
term.measure()
term.disp_temp()
term.turn_off