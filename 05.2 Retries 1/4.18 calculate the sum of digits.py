def calc_digits():
    numberlist = list(input("Enter a number: "))
    intlist = map(int,numberlist)
    return sum(intlist)


print(calc_digits())