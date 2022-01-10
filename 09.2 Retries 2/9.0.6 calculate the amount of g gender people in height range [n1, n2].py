def f6(g, n1, n2):
    import csv
    
    counter = 0
    
    with open("people.csv") as file:
        reader = csv.DictReader(file)
        
        for person in reader:
            if person["gender"] == g and (n1 <= int(person["height"]) <= n2):
                counter += 1
    
    return counter

print(f6("Female",160,180))