import csv
with open("7.23 students.txt") as studentlist:
     reader = csv.DictReader(studentlist)
     for row in reader:
         if int(row["age"]) < 30:
             print(row["first_name"], row["last_name"], row["email"])