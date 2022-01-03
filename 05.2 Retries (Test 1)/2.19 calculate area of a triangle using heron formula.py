def calc_area():
    a = float(input('Enter first side of a triangle: '))
    b = float(input('Enter second side of a triangle: '))
    c = float(input('Enter third side of a triangle: '))

    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    print(f'area of a triangle with sides {round(a,2)}, {round(b,2)}, {round(c,2)} is {round(area,2)}')
    
    
calc_area()
    