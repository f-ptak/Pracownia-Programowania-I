class Statistics():
    def __init__(self):
        self.set = []
        self.switches = []
   
    def disp_set(self):
        if len(self.set) == 0:
            print("Set: empty")
        else:
            print("Set:", end=" ")
            for i in range(len(self.set)):
                print(self.set[i], end=" ")
            print()
   
    def add_num(self):
        number = 1
        while number != 0:
            number = int(input("Enter a number: "))
            if number !=0:
                self.set.append(number)
    
    def deter_great(self):
        try:
            self.greatest = self.set[0]
            for g in range(len(self.set)):
                if self.set[g] > self.greatest:
                    self.greatest = self.set[g]
            self.switches.append("greatswitch")
        except:
            pass
        
    def deter_small(self):
        try:
            self.smallest = self.set[0]
            for g in range(len(self.set)):
                if self.set[g] < self.smallest:
                    self.smallest = self.set[g]
            self.switches.append("smallswitch")
        except:
            pass
        
    def calc_mean(self):
        try:
            self.mean = sum(self.set)/len(self.set)
            self.switches.append("meanswitch")
        except:
            pass
        
    def calc_median(self):
        try:
            b = 0
            while b < len(self.set)-1:
                d=0
                while d < len(self.set)-1:
                    if self.set[d] > self.set[d+1]:
                        temp = self.set[d+1]
                        self.set[d+1] = self.set[d]
                        self.set[d] = temp
                    d+=1
                b+=1
            if len(self.set) % 2 == 0:
                self.median = round((self.set[(len(self.set)//2)-1]+self.set[len(self.set)//2])/2,1)
            else:
                self.median = self.set[len(self.set)//2]
            self.switches.append("medswitch")
        except:
            pass
        
    def disp_stats(self):
        print("===================")
        print("Stats:")
        if "greatswitch" in self.switches: print(f"Greatest number: {self.greatest}")
        if "smallswitch" in self.switches: print(f"Smallest number: {self.smallest}")
        if "meanswitch" in self.switches: print(f"Arithmetic mean: {self.mean}")
        if "medswitch" in self.switches: print(f"Median: {self.median}")
        print("===================")

stats = Statistics()

stats.disp_set()
stats.add_num()
stats.disp_set()
stats.deter_small()
stats.calc_median()
stats.disp_stats()
stats.calc_mean()
stats.deter_great()
stats.disp_stats()