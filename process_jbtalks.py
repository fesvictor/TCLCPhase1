from AnalysisLib.ProcessFile import ProcessCariData
from ReadParameterFile import get_parameter_dict
import csv

param = get_parameter_dict()
print(param['carinet.files'])
others_list = ProcessCariData(param['carinet.files'])
print(others_list)