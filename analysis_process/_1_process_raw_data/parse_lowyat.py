import csv
import pandas
from bs4 import UnicodeDammit
from pprint import pprint
from analysis_process.Post import Post

def parse_lowyat(file_path):
    result = []
    result.append(read_title(file_path))
    with open(file_path, 'r', errors='ignore') as csvfile:
        df = pandas.read_csv(csvfile, skiprows=[0])
        for index, row in df.iterrows():
            p = Post()
            p.date = str(row['date'])
            p.value = row['text']
            p.source = 'lowyat'
            result.append(p)

    return result

def read_title(file_path):
    with open(file_path, 'r', errors='ignore') as csvfile:
        df = pandas.read_csv(csvfile)
        first_row = list(df)
        p = Post()
        p.value = first_row[0].split(':')[1].strip()
        p.date = first_row[1].split(':')[1].split(',')[0].strip()
        p.source = 'lowyat'
        return p
