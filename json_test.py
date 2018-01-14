from AnalysisLib.ProcessFile import scale_database
from AnalysisLib.Scale import search_scale
from ReadParameterFile import get_parameter_dict
param = get_parameter_dict()
word = ['我们不一样']

if search_scale('Polarity', 1, word[0], 'chinese'):
    print('hi')