def process_tweet_data(FilePath):
    from os import listdir
    from pandas import read_csv
    from io import StringIO
    word_list = []
    lookup_table = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08','Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'} 
    for FileName in listdir(FilePath): 
            with open(FilePath + "/" + FileName, encoding = 'utf-8') as InFile: 
                print(FileName)
                k = InFile.read()
                if '\n=======\n' in k:
                    k = k.split('\n=======\n')
                    k[0] = k[0].replace('<<<<<<< HEAD','')
                    k[1] = k[1].replace('>>>>>>> analysis','')
                else:
                    k = [k]                    
                for j in k:
                    df = read_csv(StringIO(j))                
                    for index, row in df.iterrows(): 
                        try:
                            _date = df.loc[index]['created_at'].split(" ") 
                            word_list.append([df.loc[index]['text'], _date[2],lookup_table[_date[1]],_date[5][2:]]) 
                            #print('tweet:', df.loc[index]['text'], _date)
                        except KeyError: 
                            pass              
    #print(word_list) 
    return word_list

#import os
#os.chdir('C:/Users/tanhongzher/Documents/GitHub')
#from TCLCPhase1.get_parameter_dict import get_parameter_dict
#param = get_parameter_dict()
#hi = process_tweet_data('TCLCPhase1/' + param['twitter.files'])