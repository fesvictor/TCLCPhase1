from AnalysisLib.ProcessFile import getObjectList, UpdateRecord, ProcessJsonData, ProcessFbData, ProcessMalaysiaKiniData, ProcessLowyatData, getDirInTemp
from AnalysisLib.Scale import search_scale
from ReadParameterFile import get_parameter_dict
from AnalysisLib import Year

def getResult():
    yearTable = {}
    word_list = []
    word_list += ProcessJsonData(param["json.files"])
    word_list += ProcessFbData(param["facebook.files"])
    word_list += ProcessMalaysiaKiniData(param["malaysiakini.files"])
    word_list += ProcessLowyatData(param["lowyat.files"])
    
    for word in word_list:  #process every sentence
        word[0] = word[0].lower()
        for party in party_list: #search if any party name in the sentence
            if party.getName() in word[0]: # if sentence contains words found in scale database
                #attitude likert scale
                if search_scale("Attitude",1,word[0]): # search whether this word in database
                    print("p")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], party.getName(), 0, "party")
                elif search_scale("Attitude",2,word[0]):
                    print("p")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], party.getName(), 1, "party")
                elif search_scale("Attitude",3,word[0]):
                    print("p")
                    print(word[3], word[2], word[1], party.getName(), 0, "party")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], party.getName(), 2, "party")
                
        for govtPolicy in govtPolicy_list: 
            if govtPolicy.getName() in word[0]: 
                #perception likert scale
                if search_scale("Perception",1,word[0]): 
                    print("g")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 0, "policy")
                elif search_scale("Perception",2,word[0]):
                    print("g")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 1, "policy")
                elif search_scale("Perception",3,word[0]):
                    print("g")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 2, "policy")
                elif search_scale("Perception",4,word[0]):
                    print("g")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 3, "policy")
                elif search_scale("Perception",5,word[0]):
                    print("g")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 4, "policy")
                
        for leader in leader_list: 
            if leader.getName() in word[0]: 
                #popularity likert scale
                if search_scale("Popularity", 1, word[0]):
                    print("l")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], leader.getName(), 0, "leader")
                elif search_scale("Popularity", 2, word[0]):
                    print("l")
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], leader.getName(), 1, "leader")
                break
            else:
                continue
    return yearTable

def printResult():
    print('\033[4m' + "Today's Result" + '\033[0m')
    print("attitude:")#attitude
    for party in party_list: #can exclude this/for printing purpuse
        print('\033[4m' + party.getName() + '\033[0m')
        for index, scale in enumerate(party.getScale(), 1):
            print("Scale", index, ": ", scale , " response")
    
    print("perception:")#perception
    for govtPolicy in govtPolicy_list:
        print('\033[4m' + govtPolicy.getName() + '\033[0m')
        for index, scale in enumerate(govtPolicy.getScale(), 1):
            print("Scale", index, ": ", scale , " response")
        
    print("popularity:")#popularity
    for leader in leader_list:
        print('\033[4m' + leader.getName() + '\033[0m')
        for index, scale in enumerate(leader.getScale(), 1):
            print("Scale", index, ": ", scale , " response")

##main program
param = get_parameter_dict()
party_list = getObjectList("Party", param["target"] + '/party.txt')
govtPolicy_list = getObjectList("GovtPolicy", param["target"] + '/govtPolicy.txt')
leader_list = getObjectList("Leader", param["target"] + '/leader.txt')

tt = getResult()
#printResult()
print(tt)
#_location = getDirInTemp(param["temp.dir"])

UpdateRecord(param['temp.dir'], tt)
#UpdateRecord(_location + '/attitudes.csv', party_list)
#UpdateRecord(_location + '/perceptions.csv', govtPolicy_list)
#UpdateRecord(_location + '/popularity.csv', leader_list)