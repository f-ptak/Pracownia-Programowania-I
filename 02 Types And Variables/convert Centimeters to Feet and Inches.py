print('Your height in centimeters: ')
Centimeters = input()
conv_Centimeters = float(Centimeters)

All_Inches = conv_Centimeters * 0.39
Feet = All_Inches // 12
Inches = round(All_Inches % 12, 2)

print('I am {} cm tall, i.e. {} feet and {} inches'.format(Centimeters, Feet, Inches))