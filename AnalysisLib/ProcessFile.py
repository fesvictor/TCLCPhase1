def scale_database(FileName):
    scale_words = []
    with open(FileName, "rb")as scale_file:
        for line in scale_file:
            scale_words.append(line.decode('utf-8').replace('\r\n',''))   
    return scale_words

def getDirInTemp(_dir): #(replcaed)
    from os import makedirs
    from os.path import exists
    from time import strftime
    if not exists(_dir + "/" + strftime("%Y") + "/" + strftime("%B")):
        makedirs(_dir + "/" + strftime("%Y") + "/" + strftime("%B"))
    return _dir + "/" + strftime("%Y") + "/" + strftime("%B")

def getObjectList(ObjectType, FileName): #get data from record file(replaced)
    if ObjectType == "Party":
        from AnalysisLib.Party import instantObject
    elif ObjectType == "GovtPolicy":
        from AnalysisLib.GovtPolicy import instantObject
    elif ObjectType == "Leader":
        from AnalysisLib.Leader import instantObject
    object_list = []
    with open(FileName) as record_file:
        for row in record_file.read().splitlines():
            object_list.append(instantObject(row))
    return object_list

def UpdateRecord(_location, _table):
    year_list = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17']
    month_list = ['00', '01', '02','03','04','05','06','07','08','09','10','11','12']
    day_list = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    for _year in year_list:
        if _year in _table:
            for _month in month_list:
                if _month in _table[_year]:
                    if _table[_year][_month] != {}:
                        with open(_location + '/' + _year + '_' + _month + '.csv', 'w') as outFile:
                            outFile.write("name,scale,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31")
                            for key, value in _table[_year][_month].items():
                                for i, x in enumerate(value['01'], 0):
                                    outFile.write('\n')
                                    outFile.write(key + ',' + str(i+1) + ',' + str(value['01'][i]) + ',' + str(value['02'][i]) + ','+ str(value['03'][i]) + ','+ str(value['04'][i]) + ','+ str(value['05'][i]) + ','+ str(value['06'][i]) + ','+ str(value['07'][i]) + ','+ str(value['08'][i]) + ','+ str(value['09'][i]) + ','+ str(value['10'][i]) + ','+ str(value['11'][i]) + ','+ str(value['12'][i]) + ','+ str(value['13'][i]) + ','+ str(value['14'][i]) + ','+ str(value['15'][i]) + ','+ str(value['16'][i]) + ','+ str(value['17'][i]) + ','+ str(value['18'][i]) + ','+ str(value['19'][i]) + ','+ str(value['20'][i]) + ','+ str(value['21'][i]) + ','+ str(value['22'][i]) + ','+ str(value['23'][i]) + ','+ str(value['24'][i]) + ','+ str(value['25'][i]) + ','+ str(value['26'][i]) + ','+ str(value['27'][i]) + ','+ str(value['28'][i]) + ','+ str(value['29'][i]) + ','+ str(value['30'][i]) + ','+ str(value['31'][i]))
                                    
        else:
            pass

def xUpdateRecord(FileName, object_list): #update the record file(replaced)
    from time import strftime
    import pandas as pd
    _day = strftime("%d")
    try:
        with open(FileName, "r") as inFile:
            df = pd.read_csv(inFile)
            
        record_dict = df.set_index("name").to_dict()
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
                
def ProcessJsonData(FilePath): #process json format scrapped data
    from os import listdir
    from json import loads
    word_list = []
    lookup_table = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08','Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName) as InFile:
            for line in InFile:
                data = loads(line)
                _time = data['created_at'].split()
                word_list.append([data['text'], _time[2],lookup_table[_time[1]],_time[5][2:]])
#    print(word_list)
    return word_list

def ProcessFbData(FilePath): #process facebook csv scrapped data
    from pandas import read_csv
    from os import listdir
    from ast import literal_eval
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName) as InFile:
            df = read_csv(InFile)
            for index, row in df.iterrows():
                _text = df.loc[index]['status_message']
                _date = df.loc[index]['status_published']
                _date = _date.split(" ")
                _date = _date[0].split("-")
                if len(_date[0]) == 1:                        
                        _date[0] = '0' + _date[0]
                try:
                    if _text is not "":
                        word_list.append([literal_eval(_text).decode('utf-8'), _date[2], _date[1], _date[0][2:]])
                except ValueError: #skip nan type
                    pass
  #  print(word_list)                
    return word_list

def ProcessMalaysiaKiniData(FilePath): #process malaysiakini scrapped data
    from os import listdir
    from pandas import read_csv
    word_list = []
    lookup_table = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08','Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName, encoding='UTF-8') as InFile:
            df = read_csv(InFile)
            for index, row in df.iterrows():
                _date = df.loc[index]['created_at'].split(" ")
                word_list.append([df.loc[index]['text'], _date[2],lookup_table[_date[1]],_date[5][2:]])
#    print(word_list)
    return word_list

def ProcessLowyatData(FilePath): #process lowyat scrapped data
    from os import listdir
    from pandas import read_csv
    word_list = []
    lookup_table = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08','Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName) as InFile:
            df = read_csv(InFile)
            for index, row in df.iterrows():
                _text = df.loc[index]['text']
                _time = df.loc[index]['time']
                _time = _time.replace(",","").split(" ")
                if _time[2] in lookup_table:
                    if len(_time[3]) == 1:                        
                        _time[3] = '0' + _time[3]
                    try:
                        if not isinstance(_text, float):
                            if _text is not "":
                                word_list.append([_text,_time[3],lookup_table[_time[2]],_time[4][2:]])
                    except ValueError: #skip nan type
                        pass
#    print(word_list)
    return word_list