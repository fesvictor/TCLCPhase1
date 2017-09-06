import matplotlib.pyplot as plt
import pandas as pd
import datetime



pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', -1)
pd.options.display.chop_threshold = None
pd.options.display.expand_frame_repr = False

def convert_day_to_date(day):
    date = datetime.datetime.strptime(day, '%d')
    date = datetime.datetime.strftime(date, '%d')
    date = '2017/01/' + date
    return date

def get_single_scale(df, scale):
    _df = df.loc[df['scale'] == scale].set_index('name').reset_index()
    return _df

def process_single_name(df, name):
    _df = df.loc[df['name'] == name].set_index('name').reset_index()
    return _df

def process_each_date(df, date_str):
    _dates = []
    _df = df.iloc[:,2:].transpose().reset_index()
    _df.columns = ['date','values']
    for d in _df['date']:
        _date = convert_day_to_date(d)
        _dates.append(_date)
    
    _df['date'] = _dates
    _df = _df.set_index('date')
    _df.index = pd.to_datetime(_df.index)
    print(_df)
    _df = _df.resample('W').sum()
    print(_df)
    
    

df = pd.read_csv('temp/facebook/party/2017_01_facebook_party.csv')

#date_d = df.columns[2:]
#new_date = []
#for _ in date_d:
#    _date = datetime.datetime.strptime(_, '%d')
#    _date = datetime.datetime.strftime(_date, '%d')
#    new_date.append('2017/01/'+_date)
#new_header = list(df.columns.values[:2]) + new_date
#df.columns = new_header
#df = df.loc[df['scale'] == 1].set_index('name').reset_index()
#print(df)

_df = get_single_scale(df, 1)
_df = process_single_name(_df, 'amanah')
_df = process_each_date(_df, '2017/01/')