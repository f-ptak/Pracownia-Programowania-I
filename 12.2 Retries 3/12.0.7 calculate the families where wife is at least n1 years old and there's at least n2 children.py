class C():
    import json
    
    with open("mockdata.json") as file:
        families = json.load(file)
    
    def m(self, n1, n2):
        counter = 0
        for family in self.families:
            if family["wife"]["age"] >= n1 and len(family["children"]) >= n2:
                counter += 1
        
        return counter 
    
    def m2(self, n1):
        import json
        dic = []
        
        for family in self.families:
            if len(family["children"]) >= n1:
                dic.append(family)
        
        with open("mockdata1.json", "w") as file:
            json.dump(dic, file, indent = 4)

print(C().m(31, 3))
C().m2(3)