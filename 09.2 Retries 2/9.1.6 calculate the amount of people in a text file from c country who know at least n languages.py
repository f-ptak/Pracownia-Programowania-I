def f6(c,n):
    import json
    
    counter = 0
    
    with open("students.json") as file:
        content = json.load(file)
    
    for person in content["students"]:
        if person["country"] == c and len(person["languages"]) >= n:
            counter += 1
    
    return counter

print(  f6("Poland",2)  )
print(  f6("Germany",1)  )