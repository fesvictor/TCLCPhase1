from AnalysisLib.ProcessFile import GetPartyRecord, UpdatePartyRecord, ProcessJsonData, ProcessFbData, ProcessMalaysiaKiniData
from AnalysisLib.Scale import search_scale
from ReadParameterFile import get_parameter_dict

##main program##
param = get_parameter_dict()
#get all partys previous information and the header format
party_list, _header = GetPartyRecord(param["temp.dir"] + '/recordss.csv')

word_list = []
word_list += ProcessJsonData(param["json.files"])
word_list += ProcessFbData(param["facebook.files"])
word_list += ProcessMalaysiaKiniData(param["malaysiakini.files"])

for word in word_list:  #process every sentence 
    for party in party_list: #search if any party name in the sentence
        if party.getName() in word: # if sentence contains words found in scale database
            #attitude likert scale
            if search_scale("Attitude",1,word): # search whether this word in database
                party.increAttScale1()
            elif search_scale("Attitude",2,word):
                party.increAttScale2()
            elif search_scale("Attitude",3,word):
                party.increAttScale3()
            #perception likert scale
            if search_scale("Perception",1,word): 
                party.increPercepScale1()
            elif search_scale("Perception",2,word):
                party.increPercepScale2()
            elif search_scale("Perception",3,word):
                party.increPercepScale3()
            elif search_scale("Perception",4,word):
                party.increPercepScale4()
            elif search_scale("Perception",5,word):
                party.increPercepScale5()
            #popularity likert scale
            if search_scale("Popularity",1,word):
                party.increPop()
            elif search_scale("Popularity",2,word):
                party.increNotPop()
            break
        else:
            continue

for party in party_list: #can exclude this/for printing purpuse
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

UpdatePartyRecord(param["output.dir"]+ '/recordss.csv', _header, party_list)