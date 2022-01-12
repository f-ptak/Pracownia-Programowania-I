class C():
    def m(self, n1, n2):
        import xml.etree.ElementTree as ET
    
        tree = ET.parse("mockdata.xml")
        root = tree.getroot()
        print(root)
        
        counter = 0
        for family in root:
            
            wife = family.find("wife")
            children = family.find("children")
            if (  int(wife.find("age").text) >= n1  ) and (  len(children) >= n2  ):
                counter += 1
        
        return counter


print(C().m(40,2))