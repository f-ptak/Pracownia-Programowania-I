x = float(input('Enter x number: '))
y =  float(input('Enter y: '))

if x>0 and y>0:
    quadrant = 'first'
elif x<0 and y>0:
    quadrant = 'second'
elif x<0 and y<0:
    quadrant = 'third'
elif x>0 and y<0:
    quadrant = 'fourth'

if x==0:
    axis = 'OY'
elif y==0:
   axis = 'OX' 

if x!=0 and y!=0:
    print(f'Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system')
elif x==0 or y==0:
    print(f'Point P({x},{y}) is located on {axis} axis')
elif x==0 and y==0:
    print('Point P is located in the (0,0) position')