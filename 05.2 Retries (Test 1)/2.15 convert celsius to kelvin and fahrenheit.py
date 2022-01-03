#Write a program that reads the temperature in degrees Celsius from the keyboard.
#The program then calculates and displays the temperature in Kelvin and Fahrenheit.

def convert_temp():
    celc = float(input('enter the temperature in Celsius: '))
    kelv = celc + 273.15
    fahr = celc * 1.8 + 32 
    print(f'{celc} degrees in Celsius is {kelv} degrees in Kelvin and {fahr} degrees in Fahrenheit')
    
    
convert_temp()