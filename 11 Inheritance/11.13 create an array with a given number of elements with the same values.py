class Arrays():
    @staticmethod
    def samevalues(elenum, eleval):
        sameray = []
        for i in range(elenum):
            sameray.append(eleval)
        return sameray
    
    @staticmethod
    def randomvalues(elenum, valfrom, valto):
        import random
        randray = []
        for i in range(elenum):
            randray.append(random.randint(valfrom,valto))
        return randray
    
    @staticmethod
    def rangevalues(array, valfrom, valto):
        counter = 0
        for i in range(len(array)):
            if valfrom <= array[i] <= valto:
                counter += 1
        return counter

print(Arrays.samevalues(10,4))
randson = Arrays.randomvalues(20,-7,8)
print(randson)
print(Arrays.rangevalues(randson,-1,1))