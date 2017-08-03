import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import numpy as np

def plot_perception():
    
#    df = pd.read_csv('temp/2017/July/perceptions.csv')
#    ax = df.pivot(index='name', columns='scale', values='1')
#    ax = ax.plot(kind = 'bar', figsize=(11,3))
#    ax.set_yticks([1,2])
#    ax.set_ylabel("Counts")
#    ax.set_xlabel("Government Policy")
#    ax.set_title("Perception\n Date: July 01")
#    ax.legend(bbox_to_anchor=(1.13, 1.03))
    my_dpi = 70#96
    
    df = pd.read_csv('temp/2017/July/perceptions.csv')
    
#    df1 = df.pivot(index='name', columns='scale', values='1')
#    df2 = df.pivot(index='name', columns='scale', values='2')
    
    fig, axes = plt.subplots(nrows=4, ncols=10, figsize=(1920/my_dpi, 1080/my_dpi), dpi=my_dpi, sharey=True, sharex=True)
    fig.autofmt_xdate(rotation=90, ha='right')
    fig.suptitle("Perceptions (July)", y=0.92, fontsize=18)
    
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
    plt.xlabel("Government Policy", labelpad=90)
    plt.ylabel("Count")
    plt.subplots_adjust(hspace=0.15, wspace=0.1)
    
    
    for i in range(1,11):
        df1 = df.pivot(index='name', columns='scale', values=str(i))
        splt1 = df1.plot(ax=axes[0,i-1], kind='bar')
        splt1.set_ylabel("")
        splt1.set_xlabel("")
        splt1.set_yticks([0,10,20,30,40])
        splt1.legend().remove()
        splt1.set_title("Day "+str(i))
        
    for i in range(1,11):
        df1 = df.pivot(index='name', columns='scale', values=str(i+10))
        splt1 = df1.plot(ax=axes[1,i-1], kind='bar')
        splt1.set_ylabel("")
        splt1.set_xlabel("")
        #splt1.set_yticks([1,2,3,4,5])
        splt1.legend().remove()
        splt1.set_title("Day "+str(i+10))
        
    for i in range(1,11):
        df1 = df.pivot(index='name', columns='scale', values=str(i+20))
        splt1 = df1.plot(ax=axes[2,i-1], kind='bar')
        splt1.set_ylabel("")
        splt1.set_xlabel("")
        #splt1.set_yticks([1,2,3,4,5])
        splt1.legend().remove()
        splt1.set_title("Day "+str(i+20))
        
    for i in range(1,2):
        df1 = df.pivot(index='name', columns='scale', values=str(i+30))
        splt1 = df1.plot(ax=axes[3,i-1], kind='bar')
        splt1.set_ylabel("")
        splt1.set_xlabel("")
        #splt1.set_yticks([1,2,3,4,5])
        splt1.legend().remove()
        splt1.set_title("Day "+str(i+30))
    
#    splt2 = df2.plot(ax=axes[0,1], kind='bar')
#    splt2.set_ylabel("")
#    splt2.set_xlabel("")
#    splt2.legend(bbox_to_anchor=(1.02, 1.03))
#    splt2.legend().remove()
    
    plt.savefig('temp.png', bbox_inches='tight')
        
#Main
plot_perception()