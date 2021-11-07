def f2():
    import random
    one = random.randrange(0,999)
    two = random.randrange(0,999)
    if one > two:
        return "tak"
    else:
        return "nie"