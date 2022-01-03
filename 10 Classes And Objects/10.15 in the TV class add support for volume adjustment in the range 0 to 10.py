class Television():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f"TV is on, Volume: {self.volume}, Channel {self.channel_no}", end="")
            if len(self.channels) == 0:
                pass
            elif self.channel_no <= len(self.channels):
                print(f" ({self.channels[self.channel_no-1]})", end="")
            print()
        else:
            print(f"TV is off")
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    def add_channel(self, new_channel):
        self.channels.append(new_channel)
    def show_channels(self):
        if len(self.channels) == 0:
            print("TV not programmed, no available channels")
        else:
            print("Channel list:")
            for i in range(len(self.channels)):
                print(f"{i+1}. {self.channels[i]}")
    def volume_up(self):
        if self.volume != 10:
            self.volume+=1
        else:
            pass
    def volume_down(self):
        if self.volume != 0:
            self.volume-=1
        else:
            pass


tv = Television()

tv.show_status()
tv.turn_on()
tv.show_status()
tv.show_channels()
tv.add_channel("TVP1")
tv.add_channel("TVP2")
tv.add_channel("Polsat")
tv.add_channel("TVN")
tv.add_channel("Filmbox")
tv.add_channel("Discovery")
tv.show_channels()
tv.show_status()
tv.set_channel(1)
tv.show_status()
tv.set_channel(2)
tv.volume_up()
tv.show_status()
tv.set_channel(3)
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.show_status()
tv.set_channel(4)
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.show_status()
tv.set_channel(5)
tv.volume_down()
tv.volume_down()
tv.volume_down()
tv.show_status()
tv.set_channel(6)
tv.volume_down()
tv.volume_down()
tv.volume_down()
tv.volume_down()
tv.volume_down()
tv.show_status()
tv.set_channel(7)
tv.volume_down()
tv.volume_down()
tv.volume_down()
tv.show_status()
tv.turn_off()
tv.show_status()