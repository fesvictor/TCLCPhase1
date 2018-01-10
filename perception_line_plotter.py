import matplotlib.pyplot as plt
import pandas as pd
import re
import datetime
import numpy as np

def add_subplots(df, axes, name_key):
    df = df.loc[df['name'] == name_key]
    df_ = df.transpose().drop('name').drop('scale')
#    mpl.style.use('default')
    this_ax = df_.plot(ax=axes, color = ['C1','C2'], xticks=np.arange(0,31,2))
    this_ax.set_title(name_key.upper())
    this_ax.legend().remove()
    this_ax.yaxis.grid(True)

def new_figure(my_dpi, df_main, date_str):
    fig, axes = plt.subplots(nrows=5, ncols=4, figsize=(3840/my_dpi, 2160/my_dpi), dpi=my_dpi, sharey=True, sharex=False)
    fig.suptitle("Polarity (Montly Trend) - " + date_str, y=0.92, fontsize=25)
    
    count = 0
    for i in range(0,5):
        for j in range(0,4):
            add_subplots(df_main, axes[i,j], df_main['name'].unique()[count])
            count += 1

    plt.subplots_adjust(hspace=0.3, wspace=0.05)
    
    lines, labels = axes[0,0].get_legend_handles_labels()
    fig.legend(lines, ['Positive','Negative'], bbox_to_anchor=(0.95, 0.885), bbox_transform=plt.gcf().transFigure)
    
    filename_datestamp = datetime.datetime.strptime(date_str, '%B %Y')
    filename_datestamp = datetime.datetime.strftime(filename_datestamp, '%Y%m')
    fig.savefig('results/polarity_output/' + filename_datestamp + '_daily_trend_01.png', bbox_inches='tight', dpi=300)

def date_converter(filename):
    date_regex = re.compile("temp/(.*).csv")
    date = date_regex.search(filename)
    date = str(date.group(1))
    date = datetime.datetime.strptime(date, '%Y_%m') #Converts string to date object
    return datetime.datetime.strftime(date, '%B %Y')

def plot_perception_line():
    plt.ioff()
    my_dpi = 150
    filename = 'temp/2017_01.csv'
    date_str = date_converter(filename)
    df_main = pd.read_csv(filename)
    new_figure(my_dpi, df_main, date_str)
    plt.close('all')
    
plot_perception_line()