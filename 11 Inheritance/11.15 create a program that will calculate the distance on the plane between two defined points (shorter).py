class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'P({self.x},{self.y})'
    
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return "The distance between the points is 0"
        else:
            exes = self.x - other.x
            whys = self.y - other.y
            distance = (exes**2 + whys**2)**(1/2)
            return "Distance between the points is: " + str(round(distance,2))

one = Point(2,2)
two = Point(2,2)
three = Point(-13,-18)
four = Point(4,-5)

print(one)
print(two)
print(three)
print(four)

print(one == two)
print(three == four)