def process_tweet_data(FilePath):
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