import matplotlib.pyplot as plt
import pandas as pd
import re
import datetime

def plot_subplots(df, axes):
    df1 = df.pivot(index='name', columns='scale', values=str(df.columns[2]))
    splt1 = df1.plot(ax=axes, kind='bar')
    splt1.set_xlabel("")
    splt1.set_xticklabels(splt1.get_xticklabels(), fontsize=10, rotation=90)
    splt1.legend().remove()
    splt1.set_title("Day "+str(df.columns[2]))

def get_top3_daily(df_main):
    top3_daily_list = []
    for i in range(1,32):
        df = df_main[['name','scale','%d'%i]]
        df_sum = df.drop('scale', axis=1)
        df_sum = df_sum.sum(axis=1, numeric_only=True)
        df_sum = pd.concat([df,df_sum], axis=1)
        df_sum = df_sum.rename(columns={0:'sum'})
        series_sum_top3 = df_sum.groupby('name')['sum'].sum().sort_values(ascending=False).reset_index().loc[[0,1,2]]
        result = df.loc[df['name'].isin(series_sum_top3['name'])]
        top3_daily_list.append(result)
    return top3_daily_list

def date_converter(filename):
    date_regex = re.compile("temp/(.*).csv")
    date = date_regex.search(filename)
    date = str(date.group(1))
    date = datetime.datetime.strptime(date, '%Y_%m') #Converts string to date object
    return datetime.datetime.strftime(date, '%B %Y')
    
def plot_perception():
    plt.ioff()
    my_dpi = 150#96
    filename = 'temp/2017_01.csv'
    date_str = date_converter(filename)
    df_main = pd.read_csv(filename)
    top3_daily_list = get_top3_daily(df_main)
    

    
#   print(top3_daily_list[0].pivot(index='name', columns='scale'))
    
    fig, axes = plt.subplots(nrows=4, ncols=10, figsize=(3840/my_dpi, 2160/my_dpi), dpi=my_dpi, sharey=True, sharex=False)
    fig.suptitle("Perceptions (Top 3 Daily) - " + date_str, y=0.92, fontsize=25)
    
    #Delete extra subplot axes
    for i in range(1,10):
        fig.delaxes(axes[3,i])
        
    for df_, ax_ in zip(top3_daily_list, axes.reshape(-1)):
        plot_subplots(df_, ax_)
    
    #Create invisible surrounding subplot for labeling purposes
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
    plt.xlabel("Name", fontsize=20)
    plt.ylabel("Count", fontsize=20)
    plt.subplots_adjust(hspace=1, wspace=0.1)
    
#    df = top3_daily_list[0]
#    df1 = top3_daily_list[0].pivot(index='name', columns='scale', values='1')
#    splt1 = df1.plot(ax=axes[0,0], kind='bar')
#    splt1.set_xlabel("")
#    splt1.set_xticklabels(splt1.get_xticklabels(), fontsize=10, rotation=45)
#    splt1.legend().remove()
#    splt1.set_title("Day "+str(df.columns[2]))
    
    #Custom legend
    lines, labels = axes[0,0].get_legend_handles_labels()
    fig.legend(lines, ['Positive','Negative'], bbox_to_anchor=(0.95, 0.885), bbox_transform=plt.gcf().transFigure)
    #Save plot
    plt.savefig('temp.png', bbox_inches='tight', dpi=300)
    plt.close(fig) #Disable console print

        
#Main
plot_perception()