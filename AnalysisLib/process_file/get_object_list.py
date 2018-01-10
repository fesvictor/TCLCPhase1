# The 2 lines below allow you to import modules from parent directory
# For more info, refer https://stackoverflow.com/questions/16780014/import-file-from-parent-directory/16780068
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TCLCPhase1.get_parameter_dict import get_parameter_dict
def get_object_list(object_type): #get data from record file(replaced)
    if object_type == "party":
        from Party import instantObject
    elif object_type == "govtPolicy":
        from GovtPolicy import instantObject
    elif object_type == "leader":
        from Leader import instantObject
    else:
         raise ValueError(object_type + "is not a recognized object_type")
    file_name = get_parameter_dict()["target"] + "/" + object_type + ".txt"
    object_list = []
    with open(file_name) as record_file:
        for row in record_file.read().splitlines():
            object_list.append(instantObject(row))
    return object_list