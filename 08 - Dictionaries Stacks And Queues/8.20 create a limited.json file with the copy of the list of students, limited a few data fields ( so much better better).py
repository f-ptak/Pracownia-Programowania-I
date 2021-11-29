import json

with open("8.20 students.json") as og, open("8.20 limited.json", "w") as lim:
    loaded = json.load(og)
    
    finalarray = []
    for val in loaded:
        row = {"name":val["name"], "surname":val["surname"], "student_id":val["student_id"]}
        finalarray.append(row)
    
    lim.write(json.dumps(finalarray, indent = 4))