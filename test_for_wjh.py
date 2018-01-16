import os
os.chdir('C:/Users/tanhongzher/Documents/GitHub')
from TCLCPhase1.AnalysisLib.process_file.get_object_list import get_object_list

party_list = get_object_list("party") 
for party in party_list:
    print(party.get_name())