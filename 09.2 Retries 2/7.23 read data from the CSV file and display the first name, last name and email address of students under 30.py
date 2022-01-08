import csv

with open("7.23 students.txt") as file:
    reader = csv.DictReader(file)
    
    for person in reader:
        if int(person["age"]) < 30:
            print(f"{person['first_name']:<10} {person['last_name']:<10} {person['email']}")