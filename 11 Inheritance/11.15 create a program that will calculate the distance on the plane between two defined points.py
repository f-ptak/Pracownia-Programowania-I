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
# ========================= calculate distance between Xs =========================
            if (self.x > 0 and other.x > 0) or (self.x < 0 and other.x < 0):
                exes = abs(abs(self.x) - abs(other.x))
            elif self.x < 0 or other.x < 0:
                exes = abs(self.x) + abs(other.x)   
# ========================= calculate distance between Ys =========================
            if (self.y > 0 and other.y > 0) or (self.y < 0 and other.y < 0):
                whys = abs(abs(self.y) - abs(other.y))
            elif self.y < 0 or other.y < 0:
                whys = abs(self.y) + abs(other.y)
# ========================= calculate distance between Points =====================
            distance = (exes**2 + whys**2)**(1/2)
            return "Distance between the points is: " + str(round(distance,2))

one = Point(2,2)
two = Point(2,2)
three = Point(-13,18)
four = Point(4,-5)

print(one)
print(two)
print(three)
print(four)

print(one == two)
print(three == four)