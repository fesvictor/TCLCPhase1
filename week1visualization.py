import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os

def autolabel(rects,ax):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height), ha='center', va='bottom')

def visualization(filename,path):
    csvfile = open(filename,"r")
    reader = csv.reader(csvfile)
    
    header = next(reader) #Stores first line as header (Currently not used, skips first line in file)
    inputdict = {}
    partylist = []
    oppose_list = []
    notsure_list = []
    consent_list = []
    response_list = []
    rect_list = []
    rect_list2 = []
    color_list = ['#E53935','#D81B60','#8E24AA','#5E35B1','#1E88E5','#039BE5','#00ACC1','#00897B','#7CB342','#C0CA33','#FDD835','#FFB300','#FB8C00','#F4511E','#6D4C41','#757575','#546E7A']
    
    for row in reader:
        partylist.append(row[0])
        inputdict[row[0]] = []
        inputdict[row[0]].append(int(row[1]))
        inputdict[row[0]].append(int(row[2]))
        inputdict[row[0]].append(int(row[3]))
        
    for n in inputdict:
        oppose_list.append(inputdict[n][0])
        notsure_list.append(inputdict[n][1])
        consent_list.append(inputdict[n][2])
        
    raw_data = {'Party':partylist,'scale1':oppose_list,'scale2':notsure_list,'scale3':consent_list}
    
    df = pd.DataFrame(raw_data, columns = ['Party','scale1','scale2','scale3'])
    
    df_list = df.values.tolist()
    
    response_list.append(oppose_list)
    response_list.append(notsure_list)
    response_list.append(consent_list)
    
    n_groups = len(inputdict)
    index = np.arange (n_groups)
    width = 0.25
    
    plt.figure(1)
    fig, ax = plt.subplots(figsize=(10,5))
    
    for i in range(0,len(response_list)):
        rect_list.append(ax.bar([p + width*i for p in index], response_list[i], width, alpha=1, color=color_list[i*4]))
        autolabel(rect_list[i],ax)
    
    ax.set_xticks([p + 1 * width for p in index])
    ax.set_xticklabels(partylist)
    plt.grid(axis='y')
    plt.legend(['Oppose','Not Sure', 'Consent'],bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0)
    ax.set_title('Grouped by Party ('+filename.split('\\')[1]+')')
    ax.set_ylabel('Count')
    ax.set_xlabel('Party')
    
    plt.savefig(path+'\\party_plot.png', bbox_inches='tight')
    
    plt.figure(2)
    fig, ax = plt.subplots(figsize=(10,5))
    
    width2 = (1 - 0.3)/len(partylist)
    index2 = np.arange(len(response_list))
    
    for i in range(0,len(partylist)):
        rect_list2.append(ax.bar([p + width2 * i for p in index2], df_list[i][1::], width2, alpha=1, color=color_list[-i*2]))
        autolabel(rect_list2[i],ax)
    
    ax.set_xticks([p + (len(partylist)/2 - 0.5) * width2 for p in index2])
    ax.set_xticklabels(['Oppose','Not Sure','Consent'])
    plt.grid(axis='y')
    plt.legend(partylist,bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0)
    ax.set_title('Grouped by Response ('+filename.split('\\')[1]+')')
    ax.set_ylabel('Count')
    ax.set_xlabel('Response')
    
    plt.savefig(path+'\\response_plot.png', bbox_inches='tight')
    #plt.show() #Plot on console
    
# Main

received_path = ('csv/') #Assuming parameter-file module temp.dir=csv/
file_format = ('*.csv')
file_list = glob.glob(received_path + file_format) #Full path will be "csv/*.csv" which gets a list of all .csv files in csv folder
for f in file_list:
    file_name = f.split('\\')[-1].split('.csv')[0]
    # Creates new path if it doesnt exist
    if not os.path.exists('output'):
        os.makedirs('output')
    save_path = 'output\\'+file_name+'_output'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    visualization(f,save_path)