import matplotlib.pyplot as plt
import pandas as pd
import re
import datetime
import os
import calendar

def plot_subplots(df, axes):
    df1 = df
    splt1 = df1.plot(ax=axes, kind='bar', color='C1')
    labels = df1['name'].tolist()
    labels = [x.upper().replace(' ','\n') for x in labels]
    splt1.set_xticklabels(labels, fontsize=8, rotation=90)
    splt1.legend().remove()
    splt1.set_title("Day "+str(df.columns[1]))

def get_top3_daily(df_main, no_of_days):
    top3_daily_list = []
    for i in range(1, no_of_days+1):
        df = df_main[['name','scale','%d'%i]]
        df_positive = df.loc[df['scale'] == 1]
        series_positive_top3 = df_positive.sort_values('%d'%i, ascending=False).reset_index().loc[[0,1,2,3,4]].drop('index', axis=1)
        series_positive_top3 = series_positive_top3.drop('scale', axis=1)
        top3_daily_list.append(series_positive_top3)
    return top3_daily_list

def date_converter(filename):
    date_regex = re.compile("temp/(.*).csv")
    date = date_regex.search(filename)
    date = str(date.group(1))
    date = datetime.datetime.strptime(date, '%Y_%m') #Converts string to date object
    return datetime.datetime.strftime(date, '%B %Y')
    
def plot_perception(filename):
    plt.ioff()
    my_dpi = 150#96
    date_str = date_converter(filename)
    df_main = pd.read_csv(filename)
    
    #Get number of days
    month = datetime.datetime.strptime(date_str, "%B %Y")
    month = datetime.datetime.strftime(month, "%#m")
    no_of_days = calendar.monthrange(2017,int(month))[1]
    
    top3_daily_list = get_top3_daily(df_main, no_of_days)
    
    
    fig, axes = plt.subplots(nrows=4, ncols=8, figsize=(3840/my_dpi, 2160/my_dpi), dpi=my_dpi, sharey=True, sharex=False)
    fig.suptitle("Polarity (Top 5 Daily Negative) - " + date_str, y=0.92, fontsize=25)
    
    #Delete extra subplot axes
    fig.delaxes(axes[3,7])
    if (no_of_days == 30):
        fig.delaxes(axes[3,6])
    if (no_of_days == 29):
        fig.delaxes(axes[3,6])
        fig.delaxes(axes[3,5])
    if (no_of_days == 28):
        fig.delaxes(axes[3,6])
        fig.delaxes(axes[3,5])
        fig.delaxes(axes[3,4])
        
    for df_, ax_ in zip(top3_daily_list, axes.reshape(-1)):
        plot_subplots(df_, ax_)
    
    #Create invisible surrounding subplot for labeling purposes
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
#    plt.xlabel("Name", fontsize=20)
    plt.ylabel("Count", fontsize=20)
    plt.subplots_adjust(hspace=0.7, wspace=0.1)
    
    #Custom legend
    lines, labels = axes[0,0].get_legend_handles_labels()
    fig.legend(lines, ['Negative'], bbox_to_anchor=(0.95, 0.885), bbox_transform=plt.gcf().transFigure)
    #Save plot
    filename_datestamp = datetime.datetime.strptime(date_str, '%B %Y')
    filename_datestamp = datetime.datetime.strftime(filename_datestamp, '%Y%m')
    plt.savefig('results/polarity_output/negative/'+filename_datestamp+'_top5_negative.png', bbox_inches='tight', dpi=300)
    plt.close('all') #Disable console print

        
#Main
    
directory = "temp/";
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.startswith("20") and filename.endswith(".csv"): 
         path = os.path.join(directory, filename)
         print("Plotting file: " + path)
         plot_perception(path)