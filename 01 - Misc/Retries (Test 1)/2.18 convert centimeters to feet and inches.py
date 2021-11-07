def convert_cm():
    cm = float(input('enter the lenght in centimeters: '))
    inch = cm * 0.39
    feet = round(inch // 12)
    rem_inch = round((inch % 12), 2)
    print(f'{cm} cm is {feet} feet and {rem_inch} inches')
    
print(convert_cm())