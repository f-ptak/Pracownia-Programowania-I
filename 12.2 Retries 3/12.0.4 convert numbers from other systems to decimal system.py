class C():
    def __init__(self, dic):
        self.dic = dic
    
    def m(self):
        system = int(self.dic["system"])
        values = []
        for i in range(len(self.dic["value"])):
            values.append(int(self.dic["value"][i]))
        
        for dig in values:
            if dig >= system:
                return -1
        
        dec = 0
        for i in range(len(values)):
#             dec += values[::-1][i] * (system**i)
            dec += values[-1-i] * (system**i)
        return dec

print(C({"system":"2", "value":"101"}).m())
print(C({"system":"8", "value":"70281"}).m())

print(C({"system":"2", "value":"101001"}).m())
print(C({"system":"3", "value":"211"}).m())
print(C({"system":"8", "value":"21"}).m())