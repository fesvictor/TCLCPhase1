#get all string with BN, DAP, PKR,govPolicy001,lim kit siang, mahathair, najib
#common between party,policy,leader
#common between all
#log count for them
from AnalysisLib.ProcessFile import ProcessJsonData, ProcessFbData, ProcessMalaysiaKiniData, ProcessLowyatData
from get_parameter_dict import get_parameter_dict

def MatchingWordFinder(_key):
    temp_list = []
    for _sentence in word_list:
        _sentence = _sentence.lower()
        if _key in _sentence:
            _sentence = _sentence.replace("\n", "")
            temp_list.append(_sentence)
    return(temp_list)

def removeName(_list, _name):
    temp_list = []
    for _word in _list:
        temp_list.append(_word.replace(_name,""))
    return temp_list
    
def getCommonExpression(_list):
    pass

def writeFile(_list, _filename):
    with open(_filename, "w", encoding='UTF-8') as OutFile:
        for _line in _list:
            if "dap" in _line:
                pass
#                print(_line)
            OutFile.write(_line)
            OutFile.write("\n")
            
param = get_parameter_dict()

word_list = []
word_list += ProcessJsonData(param["json.files"])
word_list += ProcessFbData(param["facebook.files"])
word_list += ProcessMalaysiaKiniData(param["malaysiakini.files"])
word_list += ProcessLowyatData(param["lowyat.files"])


#main program
BN_list = MatchingWordFinder("bn")
print(len(BN_list))
writeFile(BN_list, "data/temp/bn.txt")
DAP_list = MatchingWordFinder("dap")
writeFile(DAP_list, "data/temp/dap.txt")
PKR_list = MatchingWordFinder("pkr")
writeFile(PKR_list, "data/temp/pkr.txt")
KitSiang_list = MatchingWordFinder("kit siang")
writeFile(KitSiang_list, "data/temp/kitsiang.txt")
mahathair_list = MatchingWordFinder("mahathair")
writeFile(mahathair_list, "data/temp/mahathair.txt")
najib_list = MatchingWordFinder("najib")
writeFile(najib_list, "data/temp/najib.txt")
#print(BN_list)
#from pprint import pprint
#with open("data/temp/bn.txt", encoding='UTF-8') as f:
 #   pprint(f.read())

#removed_list = []
#removed_list.append(removeName(BN_list, "BN"))
#removed_list.append(removeName(DAP_list, "DAP"))
#removed_list.append(removeName(PKR_list, "PKR"))
#removed_list.append(removeName(KitSiang_list, "Kit Siang"))
#removed_list.append(removeName(mahathair_list, "Mahathair"))
#removed_list.append(removeName(najib_list, "Najib"))
#print(removed_list)