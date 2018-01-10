def get_object_list(ObjectType, FileName): #get data from record file(replaced)
    if ObjectType == "Party":
        from AnalysisLib.Party import instantObject
    elif ObjectType == "GovtPolicy":
        from AnalysisLib.GovtPolicy import instantObject
    elif ObjectType == "Leader":
        from AnalysisLib.Leader import instantObject
    object_list = []
    with open(FileName) as record_file:
        for row in record_file.read().splitlines():
            object_list.append(instantObject(row))
    return object_list