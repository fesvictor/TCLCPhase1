def process_lowyat_data(file_path): #process lowyat scrapped data
    from os import listdir
    from pandas import read_csv
    word_list = []
    lookup_table = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08','Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    for file_name in listdir(file_path):
        if file_name.startswith('lowyat'):
            #print(file_name)
            with open(file_path + "/" + file_name) as in_file:
                next(in_file)
#                in_file = open(file_path + "/" + file_name, encoding = 'utf-8')
                df = read_csv(in_file)
                for index, row in df.iterrows():
                    _text = df.loc[index]['text']
                    _time = df.loc[index]['date']
                    _time = str(_time)
                    _time = [_time[2:4],_time[4:6],_time[6:]]
                    try:
                        if not isinstance(_text, float):
                            if _text is not "":
                                word_list.append([_text,_time[2],_time[1],_time[0]])
                                #print('lowyat:', _text, _time)
                    except ValueError: #skip nan type
                        pass
    #print(word_list)
    del lookup_table
    return word_list


#import os
#os.chdir('C:/Users/tanhongzher/Documents/GitHub')
#process_lowyat_data('TCLCPhase1/data/scraperesults/lowyat')