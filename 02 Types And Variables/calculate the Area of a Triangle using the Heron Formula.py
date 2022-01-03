print('determine a: ')
s_a = input()
a = float(s_a)
print('determine b: ')
s_b = input()
b = float(s_b)
print('determine c: ')
s_c = input()
c = float(s_c)

p = (a+b+c)/2

area = (p*(p-a)*(p-b)*(p-c))**(1/2)
area_rounded= round(area, 2)

print('area: ', area_rounded)
