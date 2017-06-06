class Party:
    def __init__(self, _list):
        self.name = _list[0]
        self.scale1 = int(_list[1])
        self.scale2 = int(_list[2])
        self.scale3 = int(_list[3])

    def getName(self):
        return self.name

    def getScale(self):
        return [self.scale1, self.scale2, self.scale3]
    
    def increScale1(self):
        self.scale1 += 1
    
    def increScale2(self):
        self.scale2 += 1
    
    def increScale3(self):
        self.scale3 += 1

def createParty(Name):
    return Party(Name)
