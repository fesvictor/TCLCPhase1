def scale_database(FileName):
    scale_words = []
    with open(FileName, "rb")as scale_file:
        for line in scale_file:
            scale_words.append(line.decode('utf-8').replace('\n',''))   
    return scale_words

def GetPartyRecord(FileName): #get data from record file
    from csv import reader
    from AnalysisLib.Party import createParty
    party_list = []
    with open(FileName) as record_file:
        _header = record_file.readline()
        for row in reader(record_file):
            party_list.append(createParty(row))
    return party_list, _header

def GetLeaderRecord(FileName):
    from csv import reader
    from AnalysisLib.Leader import createLeader
    leader_list = []
    with open(FileName) as record_file:
        _header = record_file.readline()
        for row in reader(record_file):
            leader_list.append(createLeader(row))
    return leader_list, _header

def GetGovtPolicyRecord(FileName):
    from csv import reader
    from AnalysisLib.GovtPolicy import createGovtPolicy
    govt_policy_list = []
    with open(FileName) as record_file:
        _header = record_file.readline()
        for row in reader(record_file):
            govt_policy_list.append(createGovtPolicy(row))
    return govt_policy_list, _header

def UpdateRecord(FileName, _header, object_list): #update the record file
    with open(FileName, "w") as record_file:
        record_file.write(_header)
        for _object in object_list:
            record_file.write(_object.getName() + "," )
            for scale in _object.getScale():
                record_file.write(str(scale) + ",")
            record_file.write("\n")
                
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
    from csv import reader
    from os import listdir
    from ast import literal_eval
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName) as InFile:
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

def ProcessMalaysiaKiniData(FilePath): #process malaysiakini txt file
    from csv import reader
    from os import listdir
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName, encoding='UTF-8') as InFile:
            next(InFile)
            rows = reader(InFile)
            for row in rows:
                word_list.append(row[27])
    return word_list
