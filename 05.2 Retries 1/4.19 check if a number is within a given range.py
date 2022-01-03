def check_range():
    start = int(input("Enter start of the range: "))
    end = int(input("Enter end of the range: "))
    if start >= end:
        print("Wrong range")
        quit()
    number = int(input("Enter a number: "))
    if number >= start and number <= end:
        return "Yes"
    else:
        return "No"


print(check_range())