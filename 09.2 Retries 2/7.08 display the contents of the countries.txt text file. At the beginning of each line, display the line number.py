with open("7.07 countries.txt") as countries:
#     for i, country in enumerate(countries):
#           print(f"{i+1}. {country}", end="")
    
    i = 1
    for line in countries:
        print(i, line, end="")
        i += 1