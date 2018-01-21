def process_jbtalks_data(FilePath): #process jbtalks csv scrapped data
    from pandas import read_csv
    from os import listdir
    #from ast import literal_eval
    word_list = []
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName, encoding = 'utf-8') as InFile:
            df = read_csv(InFile)
            for index, row in df.iterrows():
                _text = df.loc[index]['text']
                _date = df.loc[index]['date']
                _date = _date.split(" ")
                _date = _date[0].split("-")
                if len(_date[1]) == 1:                        
                        _date[1] = '0' + _date[1]
                if len(_date[2]) == 1:                        
                        _date[2] = '0' + _date[2]
                
                #print('jbtalks:',_text,_date)
                if type(_text) == str:
    #                        word_list.append([literal_eval(_text).decode('utf-8'), _date[2], _date[1], _date[0][2:]])
                        word_list.append([_text, _date[2], _date[1], _date[0][2:]])
    #print(word_list)
    return word_list