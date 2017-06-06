class Party:
    unmatch_sentence_list = []
    def __init__(self, _list):
        self.name = _list[0]
        self.Attitude1 = int(_list[1])
        self.Attitude2 = int(_list[2])
        self.Attitude3 = int(_list[3])
        self.Perception1 = int(_list[4])
        self.Perception2 = int(_list[5])
        self.Perception3 = int(_list[6])
        self.Perception4 = int(_list[7])
        self.Perception5 = int(_list[8])
        self.Popular = int(_list[9])
        self.NotPopular = int(_list[10])

    def getName(self):
        return self.name

    def getAttScale1(self):
        return self.Attitude1
    
    def getAttScale2(self):
        return self.Attitude2
    
    def getAttScale3(self):
        return self.Attitude3
    
    def getPercepScale1(self):
        return self.Perception1
    
    def getPercepScale2(self):
        return self.Perception2
    
    def getPercepScale3(self):
        return self.Perception3
    
    def getPercepScale4(self):
        return self.Perception4
    
    def getPercepScale5(self):
        return self.Perception5
    
    def getPopular(self):
        return self.Popular
    
    def getNotPopular(self):
        return self.NotPopular
    
    def increAttScale1(self):
        self.Attitude1 += 1
    
    def increAttScale2(self):
        self.Attitude2 += 1
    
    def increAttScale3(self):
        self.Attitude3 += 1

    def increPercepScale1(self):
        self.Perception1 += 1
    
    def increPercepScale2(self):
        self.Perception2 += 1
    
    def increPercepScale3(self):
        self.Perception3 += 1
        
    def increPercepScale4(self):
        self.Perception4 += 1
        
    def increPercepScale5(self):
        self.Perception5 += 1
    
    def increPop(self):
        self.Popular += 1
    
    def increNotPop(self):
        self.NotPopular += 1
        
    def addNewSentence(self, sentence):
        self.unmatch_sentence_list.append(sentence)

def createParty(Name):
    return Party(Name)
