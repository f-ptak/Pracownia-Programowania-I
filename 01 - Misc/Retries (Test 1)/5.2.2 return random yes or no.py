def random_yesno():
    import random
    x = random.randint(0,1)
    if x == 0:
        return "Yes"
    else:
        return "No"


print(random_yesno())