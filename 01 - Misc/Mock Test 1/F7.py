def bonus(years):
    if years <= 5:
        bonus = 0
        for x in range (0,years):
            bonus += 100
        print(bonus)
    elif 5 < years <= 8:
        bonus = 500
        for x in range(0,years-5):
            bonus += 200
        print(bonus)
    else:
        bonus = 1100
        for x in range(0,years-8):
            bonus += 50
        print(bonus)