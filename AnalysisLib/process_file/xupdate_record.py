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
                