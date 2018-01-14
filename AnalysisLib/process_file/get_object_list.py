from TCLCPhase1.get_parameter_dict import get_parameter_dict


def get_object_list(object_type, folder_name=None):  # get data from record file(replaced)
    if object_type == "party":
        from TCLCPhase1.AnalysisLib.Party import Party as Instance
    elif object_type == "govt_policy":
        from TCLCPhase1.AnalysisLib.GovtPolicy import GovtPolicy as Instance
    elif object_type == "leader":
        from TCLCPhase1.AnalysisLib.Leader import Leader as Instance
    else:
        raise ValueError(object_type + " is not a recognized object_type")

    if folder_name is None:
        folder_name = "TCLCPhase1/" + get_parameter_dict()["target"] 
    folder_name += "/" + object_type + ".txt"
    object_list = []
    with open(folder_name) as record_file:
        for row in record_file.read().splitlines():
            object_list.append(Instance(row))
    return object_list
