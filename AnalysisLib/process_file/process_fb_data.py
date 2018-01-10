def process_fb_data(FilePath): #process facebook csv scrapped data
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