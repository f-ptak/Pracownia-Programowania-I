def bonus(years):
    counter = 1
    bonus = 0
    while counter <= years:
        if counter <= 5:
                bonus+=100
        elif counter > 5 and counter <= 8:
                bonus+=200
        else:
                bonus+=50
        counter+=1
    else:
        return bonus


print(bonus(9))