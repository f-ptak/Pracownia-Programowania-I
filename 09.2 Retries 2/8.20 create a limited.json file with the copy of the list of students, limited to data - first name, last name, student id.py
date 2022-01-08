import json

with open("8.20 students.json") as file:
    content = json.load(file)

arson = []

for person in content:
    dic = {  "name":person["name"], "surname":person["surname"], "student_id":person["student_id"]  }
    
    arson.append(dic)

with open("8.20 limited.json", "w") as file:
    json.dump(arson, file, indent = 4)