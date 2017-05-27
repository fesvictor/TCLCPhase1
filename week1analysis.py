from csv import reader
from ast import literal_eval
from json import loads
from pprint import pprint

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
        
def update_outfile(party_list):
    with open("recordss.csv", "w") as record_file:
        record_file.write(_header)
        for party in party_list:
            record_file.write(party.getName() + "," + str(party.getScale1()) + "," + str(party.getScale2()) + "," + str(party.getScale3()) + "\n")
        
def search_scale1(sentence):
    for words in scale1_words:
        if words in sentence:
            return True
    return False

def search_scale2(sentence):
    for words in scale2_words:
        if words in sentence:
            return True
    return False

def search_scale3(sentence):
    for words in scale3_words:
        if words in sentence:
            return True
    return False

party_list = []
with open("recordss.csv") as record_file:
    _header = record_file.readline()
    for row in reader(record_file):
        party_list.append(Party(row))
        
#main program
fb_word_list = ProcessFbData("MalaysiaKini_facebook_statuses.csv")
mk_word_list = ProcessMalaysiaKiniData("malaysiakini_20170519.csv")
json_word_list = ProcessJsonData("tweet_streams_00106.json.csv")
full_word_list = fb_word_list + mk_word_list + json_word_list

scale1_words = ["how to support ", " party not my choice", " is racist", " not Islamic", " steal money", " party for Chinese", "only oppose ", " total for Muslim", " Islamic state", " is unfair", " cannot form government", " is laughable", "Najib worst PM", "Kit Siang is communist", "Mahathir power crazy", "negative emoticons"]
scale2_words = ["whatever", "all parties are the same", "support any party for people", "all politicians are power crazy"]
scale3_words = ["like", " party", " party is for development", " party is my choice", " party deserve support", " party has done its best", " party change Malaysia for better", " party protects Malay", " party is for all Malaysian", " party has the experience", " party is clean", "Najib best", "Kit Siang hero", "Mahathir save Malaysia", "positive emoticons"]
for sentence in full_word_list:  #process every sentence
    for party in party_list: #search if any party name in the sentence
        if party.getName() in sentence: #likert scale
            if search_scale1(sentence): # if sentence contains words found in scale1 database
                party.increScale1()
                break
            elif search_scale2(sentence):
                party.increScale2()
                break
            elif search_scale3(sentence):
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

update_outfile(party_list)