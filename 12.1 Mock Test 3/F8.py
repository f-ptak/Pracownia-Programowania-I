class C():
# wszystkie metody robią to samo, tylko w inny sposób
# ta metoda za każdym razem przegląda każdą pozycję w poszukiwaniu tagu "wife" i "children"
    def m(self, n1, n2):
        import xml.etree.ElementTree as ET
        tree = ET.parse("mockdata.xml")
        root = tree.getroot()
        
        counter = 0
        for family in range(len(root)):
            wifecount = 0
            childcount = 0
            
            for person in range(len(root[family])):
                if root[family][person].tag == "wife":
                    if int(root[family][person].find("age").text) >= n1:
                        wifecount += 1
                        
                if root[family][person].tag == "children":
                    if len(root[family][person]) >= n2:
                        childcount += 1
                
            if wifecount == 1 and childcount == 1:
                counter += 1
        
        return counter

# ta metoda działa tylko, jeśli każdy zestaw danych (w tym przypadku zawartość tagu "family") ma taki sam układ
# najpierw wyznacza, na której pozycji znajduje się tag "wife" i "children", a później wykorzystuje to do szukania danych
    def m2(self, n1, n2):
        import xml.etree.ElementTree as ET
        tree = ET.parse("mockdata.xml")
        root = tree.getroot()
        
        for person in range(len(root[0])):
            if root[0][person].tag == "wife":
                wifenum = person
                break
        for person in range(len(root[0])):
            if root[0][person].tag == "children":
                childnum = person
                break
        
        counter = 0
        for family in range(len(root)):
            if int(root[family][wifenum].find("age").text) >= n1 and len(root[family][childnum]) >= n2:
                counter += 1
                
        return counter
    
# ta metoda powinna być najbardziej zoptymalizowana i wykorzystywać funkcje findall() i find(), zamiast loop'ować jak w pozostałych funkcjach
    def m3(self, n1, n2):
        import xml.etree.ElementTree as ET
        tree = ET.parse("mockdata.xml")
        root = tree.getroot()
        
        counter = 0
        for family in root.findall("family"):
            
            wife = family.find("wife")
            children = family.find("children")
            
            if int(wife.find("age").text) >= n1 and len(children) >= n2:
                counter += 1
        
        return counter

wifeage = 40
childrenamount = 2
print(C().m(wifeage, childrenamount))
print(C().m2(wifeage, childrenamount))
print(C().m3(wifeage, childrenamount))