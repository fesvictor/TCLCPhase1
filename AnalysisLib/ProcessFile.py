def scale_database(FileName):
    scale_words = []
    with open(FileName, "rb")as scale_file:
        for line in scale_file:
            scale_words.append(line.decode('utf-8').replace('\r\n',''))   
    return scale_words

def getDirInTemp(_dir):
    from os import makedirs
    from os.path import exists
    from time import strftime
    if not exists(_dir + "/" + strftime("%Y") + "/" + strftime("%B")):
        makedirs(_dir + "/" + strftime("%Y") + "/" + strftime("%B"))
    return _dir + "/" + strftime("%Y") + "/" + strftime("%B")

def GetPartyRecord(FileName): #get data from record file
    from AnalysisLib.Party import createParty
    party_list = []
    with open(FileName) as record_file:
        for row in record_file.read().splitlines():
            party_list.append(createParty(row))
    return party_list

def GetLeaderRecord(FileName):
    from AnalysisLib.Leader import createLeader
    leader_list = []
    with open(FileName) as record_file:
        for row in record_file.read().splitlines():
            leader_list.append(createLeader(row))
    return leader_list

def GetGovtPolicyRecord(FileName):
    from AnalysisLib.GovtPolicy import createGovtPolicy
    govt_policy_list = []
    with open(FileName) as record_file:
        for row in record_file.read().splitlines():
            govt_policy_list.append(createGovtPolicy(row))
    return govt_policy_list

def UpdateRecord(FileName, object_list): #update the record file
    from time import strftime
    import pandas as pd
    _day = strftime("%d")
    try:
        with open(FileName, "r") as inFile:
            df = pd.read_csv(inFile)
            
        record_dict = df.set_index("name").to_dict()
        print(record_dict)
        for _object in object_list:
                object_name = _object.getName()
                for index, scale in enumerate(_object.getScale(), 1):
                    try:
                        record_dict[_day][object_name + "(scale" + str(index) + ")"] = scale #name
                    except KeyError:
                        record_dict[_day] = {}
                        record_dict[_day][object_name + "(scale" + str(index) + ")"] = scale #name

        with open(FileName, "w") as outFile:
            outFile.write("name")
            for _key in record_dict:
                outFile.write(",")
                outFile.write(_key)
            
            for index, key in enumerate(list(list(record_dict.values())[0].keys()),0):
                outFile.write("\n")
                outFile.write((list(list(record_dict.values())[0].keys())[index]))
                for _key in record_dict:
                    outFile.write(",")
                    #list(_key.values())[index]
                    outFile.write(str(list(record_dict[_key].values())[index]))
                    #outFile.write(record_dict[_key])
                
    except FileNotFoundError:        
        with open(FileName, "w") as record_file:
            record_file.write("name," + _day) #header
            for _object in object_list:
                object_name = _object.getName()
                print(object_name)
                for index, scale in enumerate(_object.getScale(), 1):
                    record_file.write("\n" + object_name + "(scale" + str(index) + ")," + str(scale)) #scale
                
def ProcessJsonData(FilePath): #process json format file
    from os import listdir
    from json import loads
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName) as InFile:
            for line in InFile:
                data = loads(line)
                word_list.append(data['text'])
    return word_list

def ProcessFbData(FilePath): #process facebook txt file
    from pandas import read_csv
    from os import listdir
    from ast import literal_eval
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName) as InFile:
            df = read_csv(InFile)
            for index, row in df.iterrows():
                _text = df.loc[index]['status_message']
                try:
                    if _text is not "":
                        word_list.append(literal_eval(_text).decode('utf-8'))
                except ValueError:
                    pass
    return word_list

def ProcessMalaysiaKiniData(FilePath): #process malaysiakini txt file
    from os import listdir
    from pandas import read_csv
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName, encoding='UTF-8') as InFile:
            df = read_csv(InFile)
            for index, row in df.iterrows():
                word_list.append(df.loc[index]['text'])
    #print(word_list)
    return word_list

def ProcessLowyatData(FilePath):
    from os import listdir
    from pandas import read_csv
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName) as InFile:
            df = read_csv(InFile)
            for index, row in df.iterrows():
                _text = df.loc[index]['text']
                try:
                    if not isinstance(_text, float):
                        if _text is not "":
                            word_list.append(_text)
                except ValueError:
                    print("aaa")
#    print(word_list)
    return word_list