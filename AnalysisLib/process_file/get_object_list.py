from TCLCPhase1.get_parameter_dict import get_parameter_dict
def get_object_list(object_type): #get data from record file(replaced)
    if object_type == "party":
        from TCLCPhase1.AnalysisLib.Party import Party as object
    elif object_type == "govtPolicy":
        from TCLCPhase1.AnalysisLib.GovtPolicy import GovtPolicy as object
    elif object_type == "leader":
        from TCLCPhase1.AnalysisLib.Leader import Leader as object
    else:
         raise ValueError(object_type + "is not a recognized object_type")
    file_name = get_parameter_dict()["target"] + "/" + object_type + ".txt"
    object_list = []
    with open(file_name) as record_file:
        for row in record_file.read().splitlines():
            object_list.append(object(row))
    return object_list