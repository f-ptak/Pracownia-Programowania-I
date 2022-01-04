class Figures():
    @staticmethod
    def circle(rad):
        from math import pi as pi
        return pi*(rad**2)
    
    @staticmethod
    def rectangle(a, b):
        return a*b
    
    @staticmethod
    def triangle(base, height):
        return base*height/2

print(Figures.circle(3))
print(Figures.rectangle(4,7))
print(Figures.triangle(6,2))