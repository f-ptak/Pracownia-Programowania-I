import json

with open("8.20 students.json") as og, open("8.20 limited.json", "w") as lim:
    readog = og.read()
    jsoned = json.loads(readog)
    
    finalarray = []
    
    for dic in jsoned:
        tempdic = dict(dic)
        
        tempdic.pop("gender")
        tempdic.pop("age")
        tempdic.pop("year_of_study")
        tempdic.pop("email")
        
        finalarray.append(tempdic)
    
    lim.write(json.dumps(finalarray))