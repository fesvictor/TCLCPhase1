import os
import read_wordlist as rwl
import pandas as pd


def read_csv_count(file_dir):
    try:
        df = pd.read_csv(file_dir, encoding='ISO-8859-1', header=1)
        df_text = df['text'].unique()
    except:
        df = pd.read_csv(file_dir, encoding='ISO-8859-1', header=2)
        df_text = df['text'].unique()
    
    search_list = rwl.read_wordlist()
    keyword_count = 0
    
    for df_text in df['text']:
        for keyword in search_list:
            if keyword in str(df_text):
                keyword_count += 1
    
    return int(keyword_count)


directory_str = "data/scraperesults/lowyat/"
directory = os.fsencode(directory_str)
filename_list = []
keyword_count_list = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    try:
        if filename.startswith("lowyat_") and filename.endswith(".csv"):
            file_dir = os.path.join(directory_str, filename)
            count = read_csv_count(file_dir)
            filename_list.append(filename)
            keyword_count_list.append(count)
    except:
        filename_list.append(filename)
        keyword_count_list.append(-1)
    
data = list(zip(filename_list, keyword_count_list))

df = pd.DataFrame(data, columns=['filename','keyword_counts'])
df = df.sort_values(by='keyword_counts', ascending=False)
print(df)
df.to_csv("top10.csv", index=False)