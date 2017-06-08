class Leader:
    def __init__(self, _list):
        self.name = _list[0]
        self.scale1 = int(_list[1])
        self.scale2 = int(_list[2])

    def getName(self):
        return self.name
    
    def getScale(self):
        return [self.scale1, self.scale2]

    def increScale1(self):
        self.scale1 += 1
    
    def increScale2(self):
        self.scale2 += 1

def createLeader(Name):
    return Leader(Name)
