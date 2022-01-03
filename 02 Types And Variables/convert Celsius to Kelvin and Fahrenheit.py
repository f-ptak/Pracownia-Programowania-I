print('determine degrees in Celsius: ')
Celsius = input()
conv_Celsius = float(Celsius)

Kelvin = conv_Celsius + 273.15
Fahrenheit = conv_Celsius * 1.8 + 32

print ('degrees in Kelvin: {} \ndegrees in Fahrenheit: {}'.format(Kelvin, Fahrenheit))