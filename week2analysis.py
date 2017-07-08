from AnalysisLib.ProcessFile import GetPartyRecord, GetLeaderRecord, GetGovtPolicyRecord, UpdateRecord, ProcessJsonData, ProcessFbData, ProcessMalaysiaKiniData, ProcessLowyatData, getDirInTemp
from AnalysisLib.Scale import search_scale
from ReadParameterFile import get_parameter_dict

def getResult():
    word_list = []
    word_list += ProcessJsonData(param["json.files"])
    word_list += ProcessFbData(param["facebook.files"])
    word_list += ProcessMalaysiaKiniData(param["malaysiakini.files"])
    #word_list += ProcessLowyatData(param["lowyat.files"])

    for word in word_list:  #process every sentence
    
        for party in party_list: #search if any party name in the sentence
            if party.getName() in word: # if sentence contains words found in scale database
                #attitude likert scale
                if search_scale("Attitude",1,word): # search whether this word in database
                    party.increScale1()
                elif search_scale("Attitude",2,word):
                    party.increScale2()
                elif search_scale("Attitude",3,word):
                    party.increScale3()
                
    for govtPolicy in govtPolicy_list: 
        if govtPolicy.getName() in word: 
            print("2")
            #perception likert scale
            if search_scale("Perception",1,word): 
                govtPolicy.increScale1()
            elif search_scale("Perception",2,word):
                govtPolicy.increScale2()
            elif search_scale("Perception",3,word):
                govtPolicy.increScale3()
            elif search_scale("Perception",4,word):
                govtPolicy.increScale4()
            elif search_scale("Perception",5,word):
                govtPolicy.increScale5()
                
    for leader in leader_list: 
        if leader.getName() in word: 
            print("3")
            #popularity likert scale
            if search_scale("Popularity",1,word):
                leader.increScale1()
            elif search_scale("Popularity",2,word):
                leader.increScale2()
            break
        else:
            continue

def printResult():
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
party_list = GetPartyRecord(param["target"] + '/party.txt')
govtPolicy_list = GetGovtPolicyRecord(param["target"] + '/govtPolicy.txt')
leader_list = GetLeaderRecord(param["target"] + '/leader.txt')
getResult()
printResult()
_location = getDirInTemp(param["temp.dir"])

UpdateRecord(_location + '/attitudes.csv', party_list)
UpdateRecord(_location + '/perceptions.csv', govtPolicy_list)
UpdateRecord(_location + '/popularity.csv', leader_list)