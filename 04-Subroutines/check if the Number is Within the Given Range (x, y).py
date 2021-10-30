def input_ranges():
    x = int(input('Enter start of the range: '))
    y = int(input('Enter end of the range: '))
    if x >= y:
        print('ENTER A CORRECT RANGE!')
        input_ranges()
    else:
        return x,y
    
def check_range(start, end):
    if number >= start and number <= end:
        return 'Yes'
    else:
        return 'No'
    
x,y = input_ranges()
number = int(input('Enter a number: '))
print(f'Is the number {number} within the given range <{x},{y}>?')
print(check_range(x, y))