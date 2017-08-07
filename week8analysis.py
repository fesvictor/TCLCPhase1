from AnalysisLib.ProcessFile import getObjectList, UpdateRecord, ProcessJsonData, ProcessFbData, ProcessMalaysiaKiniData, ProcessLowyatData, ProcessTweetData
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
    word_list += ProcessTweetData(param["twitter.files"])
    
    for word in word_list:  #process every sentence
        word[0] = word[0].lower()
        for party in party_list: #search if any party name in the sentence
            if party.getName() in word[0]: # if sentence contains words found in scale database
                #attitude likert scale
                if search_scale("Attitude",1,word[0]): # search whether this word in database
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], party.getName(), 0, "party")
                elif search_scale("Attitude",2,word[0]):
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], party.getName(), 1, "party")
                elif search_scale("Attitude",3,word[0]):
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], party.getName(), 2, "party")
                
        for govtPolicy in govtPolicy_list: 
            if govtPolicy.getName() in word[0]: 
                #perception likert scale
                if search_scale("Perception",1,word[0]): 
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 0, "policy")
                elif search_scale("Perception",2,word[0]):
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 1, "policy")
                elif search_scale("Perception",3,word[0]):
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 2, "policy")
                elif search_scale("Perception",4,word[0]):
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 3, "policy")
                elif search_scale("Perception",5,word[0]):
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 4, "policy")
                
        for leader in leader_list: 
            if leader.getName() in word[0]: 
                #popularity likert scale
                if search_scale("Popularity", 1, word[0]):
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], leader.getName(), 0, "leader")
                elif search_scale("Popularity", 2, word[0]):
                    yearTable = Year.addScale(yearTable, word[3], word[2], word[1], leader.getName(), 1, "leader")
    return yearTable

##main program
param = get_parameter_dict()
party_list = getObjectList("Party", param["target"] + '/party.txt')
govtPolicy_list = getObjectList("GovtPolicy", param["target"] + '/govtPolicy.txt')
leader_list = getObjectList("Leader", param["target"] + '/leader.txt')

tt = getResult()
UpdateRecord(param['temp.dir'], tt)
#print(tt)
#_location = getDirInTemp(param["temp.dir"])
