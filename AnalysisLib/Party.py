class Party:
    def __init__(self, _name):
        self.name = _name
        self.scale1 = 0
        self.scale2 = 0
        self.scale3 = 0
        
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

    def __str__(self):
        return f"\nscale1 = {self.scale1}\nscale2 = {self.scale2}\nscale3 = {self.scale3}\n" 

def instantObject(Name):
    return Party(Name)
