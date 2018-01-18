def process_cari_data(FilePath): #process carinet scrapped data
    from os import listdir
    from pandas import read_csv
    word_list = []
    lookup_table = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08','Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    for FileName in listdir(FilePath): 
        if FileName.startswith('carinet'): 
            #print(FileName)
            with open(FilePath + "/" + FileName, encoding="UTF-8") as InFile:
                next(InFile)
                try:
                    df = read_csv(InFile)
                    for index, row in df.iterrows():
                        _text = df.loc[index]['text']
                        _time = df.loc[index]['date']
                        _time = str(_time)
                        _time = [_time[2:4],_time[4:6],_time[6:]]
                        print('cari:',_text,_time)
                        try:
                            if not isinstance(_text, float):
                                if _text is not "":
                                    word_list.append([_text,_time[2],_time[1],_time[0]])
                        except ValueError: #skip nan type
                            pass
                except:
                    pass
    #print(word_list)
    del lookup_table
    return word_list