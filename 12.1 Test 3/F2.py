class C():
    def __init__(self, ip):
        self.ip = ip
    
    def m(self):
        arson = self.ip.split(".")
        
        counter = self.ip.count(".")
        if counter == 3 and self.ip[0] != "." and self.ip[-1] != ".":
            for num in arson:
                if not (0 <= int(num) <= 255):
                    return False
            return True
        else:
            return False