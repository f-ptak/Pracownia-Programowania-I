def occurs(number, array):
    if number in array:
        return True
    else:
        return False

arson = [15, 38, 7, 23, 14]
num = int(input("Enter a number: "))


occurance = occurs(num, arson)

print("Number:", num)
print("Array:", arson)
print("Result:", end=" ")
if occurance:
    print(f"Number {num} appears in the array")
else:
    print(f"Number {num} does not appear in the array")