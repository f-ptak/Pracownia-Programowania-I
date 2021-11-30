def f6(g,n1,n2):
    import csv
    
    with open("people.csv") as file:
        reader = csv.DictReader(file)
        
        counter = 0
        for line in reader:
            if (line["gender"].upper() == g.upper()) and (int(line["height"]) >=160 and int(line["height"]) <=180):
                counter +=1
    return counter

print(f6("Female",160,180))