def determ_quad():
    x = int(input('Enter X: '))
    y = int(input('Enter Y: '))
    
    if x == 0 and y == 0:
        print(f'Point P ({x},{y}) is located in the center of the coordinate system')
    elif x == 0 and y != 0:
        print(f'Point P ({x},{y}) is located on the OY axis')
    elif y == 0 and x != 0:
        print(f'Point P ({x},{y}) is located on the OX axis')
    elif x > 0 and y > 0:
        print(f'Point P ({x},{y}) is located in the first quadrant')
    elif x < 0 and y > 0:
        print(f'Point P ({x},{y}) is located in the second quadrant')
    elif x < 0 and y < 0:
        print(f'Point P ({x},{y}) is located in the third quadrant')
    elif x > 0 and y < 0:
        print(f'Point P ({x},{y}) is located in the fourth quadrant')
    
determ_quad()