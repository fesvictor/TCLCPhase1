def process_json_data(FilePath): #process json format scrapped data
    from os import listdir
    from json import loads
    word_list = []
    lookup_table = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08','Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    for FileName in listdir(FilePath):
        with open(FilePath + "/" + FileName) as InFile:
            for line in InFile:
                data = loads(line)
                _time = data['created_at'].split()
                #print('json:', data['text'], _time)
                word_list.append([data['text'], _time[2],lookup_table[_time[1]],_time[5][2:]])
#    print(word_list)
    return word_list