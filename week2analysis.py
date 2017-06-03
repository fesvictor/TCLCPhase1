from csv import reader
from ast import literal_eval
from json import loads
from ReadParameterFile import get_parameter_dict
from os.path import dirname, realpath
from os import listdir

def ProcessJsonData(FilePath): #process json format file
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "\\" + FileName) as InFile:
            for line in InFile:
                data = loads(line)
                word_list.append(data['text'])
    return word_list

def ProcessFbData(FilePath): #process facebook txt file
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "\\" + FileName) as InFile:
            next(InFile)
            rows = reader(InFile)
            for row in rows:
                if row[1] is not '':
                   row[1] = literal_eval(row[1]).decode('utf-8')
                if row[2] is not '':
                   row[2] = literal_eval(row[2]).decode('utf-8')
                word_list.append(row[1])
                word_list.append(row[2])
    return word_list
    
def ProcessMalaysiaKiniData(FilePath): #process malaysiakini txt file
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "\\" + FileName, encoding='UTF-8') as InFile:
            next(InFile)
            rows = reader(InFile)
            for row in rows:
                word_list.append(row[27])
    return word_list

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

def GetPartyRecord(FileName): #get data from record file
    party_list = []
    with open(FileName) as record_file:
        _header = record_file.readline()
        for row in reader(record_file):
            party_list.append(Party(row))
    return party_list, _header
            
def UpdatePartyRecord(FileName, party_list): #update the record file
    with open(FileName, "w") as record_file:
        record_file.write(_header)
        for party in party_list:
            record_file.write(party.getName() + "," + str(party.getAttScale1()) + "," + str(party.getAttScale2()) + "," + str(party.getAttScale3()) + "," + str(party.getPercepScale1()) + "," + str(party.getPercepScale2()) + "," + str(party.getPercepScale3()) + "," + str(party.getPercepScale4()) + "," + str(party.getPercepScale5()) + "," + str(party.getPopular()) + "," + str(party.getNotPopular()) +"\n")

def search_scale(category, num, sentence): #pass the sentence to be interpreted in database
    if category == "Attitude":
        if num == 1:
            for words in att_scale1_words:
                if words in sentence:
                    return True
        elif num == 2:
            for words in att_scale2_words:
                if words in sentence:
                    return True
        elif num == 3:
            for words in att_scale3_words:
                if words in sentence:
                    return True
                
    elif category == "Perception":
        if num == 1:
            for words in percep_scale1_words:
                if words in sentence:
                    return True
        elif num == 2:
            for words in percep_scale2_words:
                if words in sentence:
                    return True
        elif num == 3:
            for words in percep_scale3_words:
                if words in sentence:
                    return True
        elif num == 4:
            for words in percep_scale4_words:
                if words in sentence:
                    return True
        elif num == 5:
            for words in percep_scale5_words:
                if words in sentence:
                    return True
    elif category == "Popularity":
        if num == 1:
            for words in popular_words:
                if words in sentence:
                    return True
        elif num == 2:
            for words in not_popular_words:
                if words in sentence:
                    return True
    return False

def scale_database(FileName):
    scale_words = []
    with open(FileName, "rb")as scale_file:
        for line in scale_file:
            scale_words.append(line.decode('utf-8').replace('\n',''))   
    return scale_words

##main program##
param = get_parameter_dict()
FilePath = dirname(realpath(__file__))
#storing words to rate the attitude scale
AttitudeFilePath = FilePath + "\\" + param['political.attitudes.scale'][2:] + '\\'
att_scale1_words = scale_database(AttitudeFilePath + "scale1.txt")
att_scale2_words = scale_database(AttitudeFilePath + "scale2.txt")
att_scale3_words = scale_database(AttitudeFilePath + "scale3.txt")
#storing words to rate the perception scale
PercepFilePath = FilePath + "\\" + param['policies.perception.scale'][2:] + '\\'
percep_scale1_words = scale_database(PercepFilePath + "scale1.txt")
percep_scale2_words = scale_database(PercepFilePath + "scale2.txt")
percep_scale3_words = scale_database(PercepFilePath + "scale3.txt")
percep_scale4_words = scale_database(PercepFilePath + "scale4.txt")
percep_scale5_words = scale_database(PercepFilePath + "scale5.txt")
#storing words to rate the popularity scale
PopFilePath = FilePath + "\\" + param['popular.political'][2:] + '\\'
popular_words = scale_database(PopFilePath + "popular.txt")
not_popular_words = scale_database(PopFilePath + "notpopular.txt")

#get all partys previous information and the header format
OutputFilePath = FilePath + "\\" + param["output.dir"][2:] + '\\recordss.csv'
party_list, _header = GetPartyRecord(OutputFilePath)

full_list = []                       
full_list += ProcessJsonData(FilePath + "\\" + param["json.files"][2:])
full_list += ProcessFbData(FilePath + "\\" + param["facebook.files"][2:])
full_list += ProcessMalaysiaKiniData(FilePath + "\\" + param["malaysiakini.files"][2:])

for sentence in full_list:  #process every sentence 
    for party in party_list: #search if any party name in the sentence
        if party.getName() in sentence: # if sentence contains words found in scale database
            #attitude likert scale
            if search_scale("Attitude",1,sentence): # search whether this word in database
                party.increAttScale1()
            elif search_scale("Attitude",2,sentence):
                party.increAttScale2()
            elif search_scale("Attitude",3,sentence):
                party.increAttScale3()
            #perception likert scale
            if search_scale("Perception",1,sentence): 
                party.increPercepScale1()
            elif search_scale("Perception",2,sentence):
                party.increPercepScale2()
            elif search_scale("Perception",3,sentence):
                party.increPercepScale3()
            elif search_scale("Perception",4,sentence):
                party.increPercepScale4()
            elif search_scale("Perception",5,sentence):
                party.increPercepScale5()
            #popularity likert scale
            if search_scale("Popularity",1,sentence):
                party.increPop()
            elif search_scale("Popularity",2,sentence):
                party.increNotPop()
            break
        else:
            continue

for party in party_list:
    print('\033[4m' + party.getName() + '\033[0m')
    print("attitude:")#attitude
    print("Scale 1: ", party.getAttScale1() , " response")
    print("Scale 2: ", party.getAttScale2() , " response")
    print("Scale 3: ", party.getAttScale3() , " response")
    print("perception:")#perception
    print("Scale 1: ", party.getPercepScale1() , " response")
    print("Scale 2: ", party.getPercepScale2() , " response")
    print("Scale 3: ", party.getPercepScale3() , " response")
    print("Scale 4: ", party.getPercepScale4() , " response")
    print("Scale 5: ", party.getPercepScale5() , " response")
    print("popularity:")#popularity
    print("Popular: ", party.getPopular() , " response")
    print("Not popular: ", party.getNotPopular() , " response")

UpdatePartyRecord(OutputFilePath, party_list)