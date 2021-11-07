#The radius of the circle has the value 5.
#Write a program that calculates the area and circumference of the circle.

def calculate_area(r):
    pi = 3.14
    area = pi * r**2
    return area
    
def calculate_circumference(r):
    pi = 3.14
    circumference = 2 * pi * r
    return circumference
    
radius = 3

print(calculate_area(radius))
print(calculate_circumference(radius))