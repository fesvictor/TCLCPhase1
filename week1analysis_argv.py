from csv import reader
from ast import literal_eval
from json import loads
import sys

def ProcessFile(FileType, FilePath):
    if FileType == 'Facebook':
        return ProcessFbData(FilePath)
    elif FileType == 'MalaysiaKini':    
        return ProcessMalaysiaKiniData(FilePath)
    elif FileType == 'Json':
        return ProcessJsonData(FilePath)
    
def ProcessJsonData(FileName): #process json format file
    word_list = []
    with open(FileName) as InFile:
        for line in InFile:
            data = loads(line)
            word_list.append(data['text'])
        return word_list

def ProcessFbData(FileName): #process facebook txt file
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
    
def ProcessMalaysiaKiniData(FileName): #process malaysiakini txt file
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
            record_file.write(party.getName() + "," + str(party.getScale1()) + "," + str(party.getScale2()) + "," + str(party.getScale3()) + "\n")
        
def search_scale(num, sentence): #pass the sentence to be interpreted in database
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

def scale_database(FileName):
    scale_words = []
    with open(FileName, "rb")as scale_file:
        for line in scale_file:
            scale_words.append(line.decode('utf-8').replace('\r\n',''))   
    return scale_words

##main program##

#storing words to rate the scale
scale1_words = scale_database("scale1.txt")
scale2_words = scale_database("scale2.txt")
scale3_words = scale_database("scale3.txt")

#get all partys previous information and the header format
party_list, _header = GetPartyRecord("recordss.csv")

full_word_list = []
#remove the python filename #argument= Facebook, MalaysiaKini_facebook_statuses.csv
argument = sys.argv[1:]              # MalaysiaKini, malaysiakini_20170519.csv
                                     # Json, tweet_streams_00106.json.csv                           
for i in range(int(len(argument)/2)):
    full_word_list += ProcessFile(argument[2*i], argument[2*i+1])
    
for sentence in full_word_list:  #process every sentence
    for party in party_list: #search if any party name in the sentence
        if party.getName() in sentence: #likert scale
            if search_scale(1,sentence): # if sentence contains words found in scale database
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