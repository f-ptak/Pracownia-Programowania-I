class C:
    def __init__(self, array):
        self.array = array
        
    def m(self):
        roznice =[]
        for x in range(len(self.array)-1):
            temp = self.array[x+1] - self.array[x]
            roznice.append(temp)
        
        ile = roznice[0]
        for y in range(1,len(roznice)):
            if ile != roznice[y]:
                return -1
        else:
            return ile

print(C([22,33,44,55,66]).m())
print(C([22,33,55,66]).m())