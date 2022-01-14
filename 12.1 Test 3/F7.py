class C():
    def m(self,n1,n2,n3):
        import json
        
        if n2 > n1:
            one = n1
            two = n2
        else:
            one = n2
            two = n1
        
        counter = 0
        
        with open("data.json") as file:
            content = json.load(file)
        
        for family in content:
            if (  one <= family["husband"]["age"] <= two  ) and (  len(family["children"]) >= n3  ):
                counter += 1
        
        return counter