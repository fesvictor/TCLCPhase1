from csv import reader
from ast import literal_eval
from json import loads
import sys

def ProcessFile(FileType, FilePath):
    if FileType == "Facebook":
        return ProcessFbData(FilePath)
    elif FileType == "MalaysiaKini":    
        return ProcessMalaysiaKiniData(FilePath)
    elif FileType == "Json":
        return ProcessJsonData(FilePath)
    
def ProcessJsonData(FileName):
    word_list = []
    with open(FileName) as InFile:
        for line in InFile:
            data = loads(line)
            word_list.append(data['text'])
        return word_list

def ProcessFbData(FileName):
    with open(FileName) as InFile:
        word_list = []
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
    
def ProcessMalaysiaKiniData(FileName):
    with open(FileName, encoding='UTF-8') as InFile:
        word_list = []
        next(InFile)
        rows = reader(InFile)
        for row in rows:
            word_list.append(row[27])
        return word_list

class Party:
    unmatch_sentence_list = []
    def __init__(self, _list):
        self.name = _list[0]
        self.scale1 = int(_list[1])
        self.scale2 = int(_list[2])
        self.scale3 = int(_list[3])

    def getName(self):
        return self.name

    def getScale1(self):
        return self.scale1
    
    def getScale2(self):
        return self.scale2
    
    def getScale3(self):
        return self.scale3

    def increScale1(self):
        self.scale1 += 1
    
    def increScale2(self):
        self.scale2 += 1
    
    def increScale3(self):
        self.scale3 += 1
    
    def addNewSentence(self, sentence):
        self.unmatch_sentence_list.append(sentence)

def GetPartyRecord(FileName):
    party_list = []
    with open(FileName) as record_file:
        _header = record_file.readline()
        for row in reader(record_file):
            party_list.append(Party(row))
    return party_list, _header
            
def UpdatePartyRecord(FileName, party_list):
    with open(FileName, "w") as record_file:
        record_file.write(_header)
        for party in party_list:
            record_file.write(party.getName() + "," + str(party.getScale1()) + "," + str(party.getScale2()) + "," + str(party.getScale3()) + "\n")
        
def search_scale(num, sentence):
    if num == 1:
        for words in scale1_words:
            if words in sentence:
                return True
    elif num == 2:
        for words in scale2_words:
            if words in sentence:
                return True
    elif num == 3:
        for words in scale3_words:
            if words in sentence:
                return True
    return False

party_list, _header = GetPartyRecord("recordss.csv")
#scale1 database
scale1_words = []
with open("scale1.txt", "rb")as scale1_file:
    for line in scale1_file:
        scale1_words.append(line.decode('utf-8').replace('\r\n',''))        
#scale2 database
scale2_words = []
with open("scale2.txt", "rb")as scale2_file:
    for line in scale2_file:
        scale2_words.append(line.decode('utf-8').replace('\r\n',''))       
#scale3 database
scale3_words = []
with open("scale3.txt", "rb")as scale3_file:
    for line in scale3_file:
        scale3_words.append(line.decode('utf-8').replace('\r\n',''))       

#main program
full_word_list = []
for i in range(int(len(sys.argv)/2)):
    full_word_list += ProcessFile(sys.argv[i],sys.argv[i+1])
print(full_word_list)
for sentence in full_word_list:  #process every sentence
    for party in party_list: #search if any party name in the sentence
        if party.getName() in sentence: #likert scale
            if search_scale(1,sentence): # if sentence contains words found in scale1 database
                party.increScale1()
                break
            elif search_scale(2,sentence):
                party.increScale2()
                break
            elif search_scale(3,sentence):
                party.increScale3()
                break
            else: 
                party.addNewSentence(sentence)
        else:
            continue

for party in party_list:
    print('\033[4m' + party.getName() + '\033[0m')
    print("Scale 1: ", party.getScale1() , " response")
    print("Scale 2: ", party.getScale2() , " response")
    print("Scale 3: ", party.getScale3() , " response")

UpdatePartyRecord("recordss.csv", party_list)