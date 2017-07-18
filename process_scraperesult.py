#get all string with BN, DAP, PKR,govPolicy001,lim kit siang, mahathair, najib
#common between party,policy,leader
#common between all
#log count for them
from AnalysisLib.ProcessFile import ProcessJsonData, ProcessFbData, ProcessMalaysiaKiniData, ProcessLowyatData
from ReadParameterFile import get_parameter_dict

def MatchingWordFinder(_key):
    temp_list = []
    for _sentence in word_list:
        if _key in _sentence:
            temp_list.append(_sentence)
    return(temp_list)

def removeName(_list, _name):
    temp_list = []
    for _word in _list:
        temp_list.append(_word.replace(_name,""))
    return temp_list
    
def getCommonExpression(_list):
    pass

param = get_parameter_dict()

word_list = []
word_list += ProcessJsonData(param["json.files"])
word_list += ProcessFbData(param["facebook.files"])
word_list += ProcessMalaysiaKiniData(param["malaysiakini.files"])
word_list += ProcessLowyatData(param["lowyat.files"])

#main program
full_list = []
BN_list = MatchingWordFinder("BN")
DAP_list = MatchingWordFinder("DAP")
PKR_list = MatchingWordFinder("PKR")
KitSiang_list = MatchingWordFinder("Kit Siang")
mahathair_list = MatchingWordFinder("Mahathair")
najib_list = MatchingWordFinder("Najib")
print(najib_list)
#print(BN_list)

removed_list = []
removed_list.append(removeName(BN_list, "BN"))
removed_list.append(removeName(DAP_list, "DAP"))
removed_list.append(removeName(PKR_list, "PKR"))
removed_list.append(removeName(KitSiang_list, "Kit Siang"))
removed_list.append(removeName(mahathair_list, "Mahathair"))
removed_list.append(removeName(najib_list, "Najib"))
#print(removed_list)