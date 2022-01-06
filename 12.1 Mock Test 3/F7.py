class C():
    import json
    with open("mockdata.json") as mockdata:
        data = json.load(mockdata)
    
    def m(self, n1, n2):
        counter = 0
        
        for dic in self.data:
            if dic["wife"]["age"] >= n1 and len(dic["children"]) >= n2:
                counter+=1
        return counter
    
    def m2(self, n1):
        import json
        with open("mockdata1.json", "w") as newdata:
            families = []
            for dic in self.data:
                if len(dic["children"]) >= n1:
                    families.append(dic)
            newdata.write(json.dumps(families,indent=4))

print(C().m(21, 2))
print(C().m2(2))