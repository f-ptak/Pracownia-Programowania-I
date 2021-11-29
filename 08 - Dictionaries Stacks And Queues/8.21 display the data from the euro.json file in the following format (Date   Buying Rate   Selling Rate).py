import json

with open("8.21 euro.json") as file, open("8.21 aaaa ughhh.json", "w") as lim:
    print("Date            Buying Rate     Selling Rate")
    print("============================================")
    
    readfile = file.read()
    jsoned = json.loads(readfile)
    ratesarray = jsoned["rates"]
    
    for line in ratesarray:
        tempdic = dict(line)
        print(tempdic["effectiveDate"], end="      ")
        print(tempdic["bid"], end="          ")
        print(tempdic["ask"])