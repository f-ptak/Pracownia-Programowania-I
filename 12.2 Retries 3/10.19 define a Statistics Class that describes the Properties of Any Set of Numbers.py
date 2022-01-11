class Statistics():
    def __init__(self):
        self.set = []
        self.switches = []
    
    def setdisplay(self):
        print("------------------------------------------------------")
        message = "Displaying content of the set:"
        print(f"{message:^50}")
        numbers = ""
        for num in self.set:
            numbers += f"{num} "
        print(f"{numbers:^50}")
        print("------------------------------------------------------\n")
    
    def calcdisplay(self):
        print("======================================================")
        if "switchGreat" in self.switches:
            messageGreat = f"Greatest number: {self.greatest}"
            print(f"{messageGreat:^50}")
        if "switchSmall" in self.switches:
            messageSmall = f"Smallest number: {self.smallest}"
            print(f"{messageSmall:^50}")
        if "switchMean" in self.switches:
            messageMean = f"Arithmetic mean: {self.mean}"
            print(f"{messageMean:^50}")
        if "switchMedian" in self.switches:
            messageMedian = f"Median: {self.median}"
            print(f"{messageMedian:^50}")
        print("======================================================\n")
    
    def add(self):
        self.set.append( int(input("Enter a number: ")) )
    
    def greatest(self):
        self.greatest = self.set[0]
        for num in self.set:
            if num > self.greatest:
                self.greatest = num
        
        self.switches.append("switchGreat")
    
    def smallest(self):
        self.smallest = self.set[0]
        for num in self.set:
            if num < self.smallest:
                self.smallest = num
        
        self.switches.append("switchSmall")
    
    def mean(self):
        self.mean = sum(self.set)/len(self.set)
        self.switches.append("switchMean")
    
    def median(self):
        for i in range(len(self.set)-1):
            for j in range(len(self.set)-1):
                if self.set[j] > self.set[j+1]:
                    temp = self.set[j]
                    self.set[j] = self.set[j+1]
                    self.set[j+1] = temp
        
        if len(self.set)%2 == 0:
            self.median = (  self.set[len(self.set)//2] + self.set[ (len(self.set)//2) -1]  ) / 2
        else:
            self.median = self.set[len(self.set)//2]
        
        self.switches.append("switchMedian")

s = Statistics()

s.add()
s.add()
s.add()
s.add()
s.add()
s.setdisplay()
s.greatest()
s.mean()
s.calcdisplay()
s.smallest()
s.median()
s.calcdisplay()