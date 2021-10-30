def calculate_sum(number):
    digits_string = list(number)
#map applies the first argument, a function, to each element in an iterable
    digits_int = map(int, digits_string)
    digits_sum = sum(digits_int)
    return digits_sum
    
    
number = input('Enter a number: ')
print(f'the sum of digits in the number {number} is', calculate_sum(number))