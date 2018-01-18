#from TCLCPhase1.get_parameter_dict import get_parameter_dict

def get_object_list(object_type, FileName, _language = 'chinese'):  # get data from record file(replaced)
    if object_type == "party":
        from TCLCPhase1.AnalysisLib.Party import Party as Instance
    elif object_type == "govt_policy":
        from TCLCPhase1.AnalysisLib.GovtPolicy import GovtPolicy as Instance
    elif object_type == "leader":
        from TCLCPhase1.AnalysisLib.Leader import Leader as Instance
    else:
        raise ValueError(object_type + " is not a recognized object_type")
        
    object_list = []
#    if _language == 'english':
#        with open('TCLCPhase1/' + FileName) as record_file:
#            for row in record_file.read().splitlines():
#                object_list.append(Instance(row))
                
#    elif _language == 'chinese':
    with open( 'TCLCPhase1/' + FileName, encoding = 'utf-8') as record_file:
        for row in record_file.read().replace('\ufeff','').splitlines():
            object_list.append(Instance(row))
    return object_list

