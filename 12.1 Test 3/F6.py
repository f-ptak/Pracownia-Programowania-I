class C():
    def __init__(self, text):
        self.text = text
    
    def m(self):
        dic = {}
        for char in self.text:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        return dic