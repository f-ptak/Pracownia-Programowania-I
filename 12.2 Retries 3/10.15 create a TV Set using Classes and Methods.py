class TV():
    def __init__(self):
        self.chanlist = []
        self.on = False
        self.curchan = 1
        self.volume = 0
    
    def show_stat(self):
        print("==================================================")
        print(f"{'Status:':^50}")
        if self.on:
            message = f"TV is on. Volume set: {self.volume}"
            print(f"{message:^50}")
            try:
                info = f"Channel {self.curchan} ({self.chanlist[self.curchan-1]})"
                print(f"{info:^50}")
            except:
                pass
        else:
            print(f"{'TV is off.':^50}")
        print("==================================================\n")
        
    def power(self):
        if self.on:
            self.on = False
        else:
            self.on = True
    
    def volup(self):
        if self.volume < 10:
            self.volume += 1
    
    def voldown(self):
        if self.volume > 0:
            self.volume -= 1
    
    def change_chan(self, num):
        self.curchan = num
        
    
    def set_chans(self, chans):
        for chan in chans:
            self.chanlist.append(chan)
    
    def show_chans(self):
        print("--------------------------------------------------")
        print(f"{'Channel list:':^50}")
        if len(self.chanlist) == 0:
            print(f"{'TV not programmed, no available channels':^50}")
            
        else:
            for i in range(len(self.chanlist)):
                print(f"{i+1}. {self.chanlist[i]}")
        print("--------------------------------------------------\n")

t = TV()

t.show_stat()
t.power()
t.voldown()
t.volup()
t.volup()
t.volup()
t.show_stat()
t.change_chan(3)
t.volup()
t.volup()
t.volup()
t.volup()
t.volup()
t.volup()
t.volup()
t.volup()
t.volup()
t.show_stat()
t.show_chans()
t.set_chans(["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"])
t.show_chans()
t.change_chan(5)
t.voldown()
t.voldown()
t.voldown()
t.voldown()
t.voldown()
t.show_stat()
t.change_chan(3)
t.voldown()
t.voldown()
t.voldown()
t.voldown()
t.voldown()
t.voldown()
t.show_stat()
t.power()
t.show_stat()