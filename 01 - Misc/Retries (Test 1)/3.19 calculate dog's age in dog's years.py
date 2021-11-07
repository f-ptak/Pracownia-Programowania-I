def calc_age():
    human_years = int(input("Enter dog's age in human years: "))
    
    dog_years = 0
    i = 1
    while i <= human_years:
        if i <= 2:
            dog_years += 10.5
        else:
            dog_years += 4
        i+=1
    
    print(f"dog's age in dog's years: {dog_years}")


calc_age()