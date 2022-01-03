def f6(c,n):
    import json
    with open("students.json") as file:
        read = file.read()
        readson = json.loads(read)
        
        counter = 0
        for dic in readson["students"]:
            if dic["country"] == c and len(dic["languages"]) >= n:
                counter+=1
    
    return counter