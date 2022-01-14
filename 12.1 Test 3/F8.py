class C():
    def m(self,n1,n2,n3):
        import xml.etree.ElementTree as ET
        tree = ET.parse("data.xml")
        root = tree.getroot()
        
        if n2 > n1:
            one = n1
            two = n2
        else:
            one = n2
            two = n1
        
        counter = 0
        for family in root:
            husband = family.find("husband")
            children = family.find("children")
            
            if (  one <= int(husband.find("age").text) <= two  ) and len(children) >= n3:
                counter += 1
        
        return counter