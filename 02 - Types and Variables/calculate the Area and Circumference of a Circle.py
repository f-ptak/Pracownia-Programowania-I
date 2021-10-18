#####
# Calculation of the area and circumference of a circle
##

# determine radius and PI
# ... program statements here ...
print('determine radius: ')
radius = input()
conv_radius = float(radius)
print('determine PI: ')
PI = input()
conv_PI = float(PI)

# calculate area 
# ... program statements here ...
area = conv_PI * (conv_radius ** 2) 

# calculate circumference 
# ... program statements here ...
circumference = 2 * conv_PI * conv_radius

# display results 
# ... program statements here ...
print('area:  {} \ncircumference: {}'.format(area, circumference))
