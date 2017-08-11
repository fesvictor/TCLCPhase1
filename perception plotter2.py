import matplotlib.pyplot as plt
import pandas as pd
import re
import datetime

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
    
    my_dpi = 70#96
    filename = 'temp/2017_01.csv'
    date_str = date_converter(filename)
    df_main = pd.read_csv(filename)
    top3_daily_list = get_top3_daily(df_main)
    
#    print(top3_daily_list[0].pivot(index='name', columns='scale'))
    
    fig, axes = plt.subplots(nrows=4, ncols=10, figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi, sharey=True, sharex=False)
    fig.autofmt_xdate(rotation=90, ha='right')
    fig.suptitle("Perceptions (Jan)", y=0.92, fontsize=18)
    
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
    plt.xlabel("Name", labelpad=90)
    plt.ylabel("Count")
    plt.subplots_adjust(hspace=0.15, wspace=0.1)
    plt.legend()
    
    df1 = top3_daily_list[0].pivot(index='name', columns='scale', values='1')
    splt1 = df1.plot(ax=axes[0,0], kind='bar')
#    splt1.set_ylabel("")
#    splt1.set_xticklabels(['a','b','c'])
    #splt1.set_yticks([0,5,10,15,20,25,30,35,40])
    splt1.legend().remove()
    splt1.set_title("Day "+str(1))
#    
#    
#    for i in range(1,11):
#        df1 = df.pivot(index='name', columns='scale', values=str(i))
#        splt1 = df1.plot(ax=axes[0,i-1], kind='bar')
#        splt1.set_ylabel("")
#        splt1.set_xlabel("")    
#        splt1.set_yticks([0,5,10,15,20,25,30,35,40])
#        splt1.legend().remove()
#        splt1.set_title("Day "+str(i))
#        
#    for i in range(1,11):
#        df1 = df.pivot(index='name', columns='scale', values=str(i+10))
#        splt1 = df1.plot(ax=axes[1,i-1], kind='bar')
#        splt1.set_ylabel("")
#        splt1.set_xlabel("")
#        #splt1.set_yticks([1,2,3,4,5])
#        splt1.legend().remove()
#        splt1.set_title("Day "+str(i+10))
#        
#    for i in range(1,11):
#        df1 = df.pivot(index='name', columns='scale', values=str(i+20))
#        splt1 = df1.plot(ax=axes[2,i-1], kind='bar')
#        splt1.set_ylabel("")
#        splt1.set_xlabel("")
#        #splt1.set_yticks([1,2,3,4,5])
#        splt1.legend().remove()
#        splt1.set_title("Day "+str(i+20))
#        
#    for i in range(1,2):
#        df1 = df.pivot(index='name', columns='scale', values=str(i+30))
#        splt1 = df1.plot(ax=axes[3,i-1], kind='bar')
#        splt1.set_ylabel("")
#        splt1.set_xlabel("")
#        #splt1.set_yticks([1,2,3,4,5])
#        splt1.legend().remove()
#        splt1.set_title("Day "+str(i+30))
#    
    splt1.legend(bbox_to_anchor=(11.05, 4), loc='lower left', borderaxespad=0.)
    
    plt.savefig('temp.png', bbox_inches='tight')
        
#Main
plot_perception()