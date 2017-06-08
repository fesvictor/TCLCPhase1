import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os
from ReadParameterFile import get_parameter_dict

def autolabel(rects,ax):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height), ha='center', va='bottom')

def visualization(filename,path):
    csvfile = open(filename,"r")
    reader = csv.reader(csvfile)
    header = next(reader) #Stores first line as header (Currently not used, skips first line in file)
    inputdict = {}
    namelist = []
    response_list = []
    rect_list = []
    rect_list2 = []
    legend = []
    color_list = ['#E53935','#D81B60','#8E24AA','#5E35B1','#1E88E5','#039BE5','#00ACC1','#00897B','#7CB342','#C0CA33','#FDD835','#FFB300','#FB8C00','#F4511E','#6D4C41','#757575','#546E7A']

    for row in reader:
        if len(row) != 0:
            namelist.append(row[0])
            inputdict[row[0]] = list(row[1::])
            inputdict[row[0]] = [int(i) for i in inputdict[row[0]]]

    #Popularity
    if header==['name','scale1','scale2']:
        notpopular_list = []
        popular_list = []
        
        for n in inputdict:
            notpopular_list.append(inputdict[n][0])
            popular_list.append(inputdict[n][1])
        
        raw_data = {'Name':namelist,'scale1':notpopular_list,'scale2':popular_list}
        df = pd.DataFrame(raw_data, columns = header)
        df_list = df.values.tolist()
        response_list.append(notpopular_list)
        response_list.append(popular_list)
        n_groups = len(inputdict)
        index = np.arange (n_groups)
        width = (1)/len(namelist)
        x_adj = 0.5
        legend = ['Not Popular','Popular']
        title1 = 'Grouped by Name'
        title2 = 'Grouped by Popularity'
        y_label1 = 'Count'
        x_label1 = 'Name'
        x_label2 = 'Popularity'
        file_name1 = 'name_plot.png'
        file_name2 = 'popularity_plot.png'
    
    #Perception on gov policies
    if header==['name','scale1','scale2','scale3','scale4','scale5']:
        burden_list = []
        n_useful_list = []
        idm_list = []
        useful_list = []
        improve_list = []
        
        for n in inputdict:
            burden_list.append(inputdict[n][0])
            n_useful_list.append(inputdict[n][1])
            idm_list.append(inputdict[n][2])
            useful_list.append(inputdict[n][3])
            improve_list.append(inputdict[n][2])
        
        raw_data = {'Policy':namelist,'scale1':burden_list,'scale2':n_useful_list,'scale3':idm_list,'scale4':useful_list,'scale5':improve_list}
        df = pd.DataFrame(raw_data, columns = header)
        df_list = df.values.tolist()
        response_list.append(burden_list)
        response_list.append(n_useful_list)
        response_list.append(idm_list)
        response_list.append(useful_list)
        response_list.append(improve_list)
        n_groups = len(inputdict)
        index = np.arange (n_groups)
        width = (1 - 0.6)/len(namelist)
        x_adj = -1
        legend = ['Burden on people','Not useful','I don\'t mind','Useful','Will improve the nation']
        title1 = 'Grouped by Policy'
        title2 = 'Grouped by Perception'
        y_label1 = 'Count'
        x_label1 = 'Policy'
        x_label2 = 'Perception'
        file_name1 = 'policy_plot.png'
        file_name2 = 'perception_plot.png'
        
    #Attitude
    if header==['name','scale1','scale2','scale3']: 
        
        oppose_list = []
        notsure_list = []
        consent_list = []
        
        for n in inputdict:
            oppose_list.append(inputdict[n][0])
            notsure_list.append(inputdict[n][1])
            consent_list.append(inputdict[n][2])
            
        raw_data = {'Party':namelist,'scale1':oppose_list,'scale2':notsure_list,'scale3':consent_list}
        df = pd.DataFrame(raw_data, columns = header)
        df_list = df.values.tolist()
        response_list.append(oppose_list)
        response_list.append(notsure_list)
        response_list.append(consent_list)
        n_groups = len(inputdict)
        index = np.arange (n_groups)
        width = (1 - 0.3)/len(namelist)
        x_adj = 0
        legend = ['Oppose','Not Sure', 'Consent']
        title1 = 'Grouped by Party'
        title2 = 'Grouped by Response'
        y_label1 = 'Count'
        x_label1 = 'Party'
        x_label2 = 'Response'
        file_name1 = 'party_plot.png'
        file_name2 = 'response_plot.png'
    
    #Plot graphs based on configuration
    #Figure 1
    plt.figure()
    fig, ax = plt.subplots(figsize=(10,5))
    
    for i in range(0,len(response_list)):
        rect_list.append(ax.bar([p + width*i for p in index], response_list[i], width, alpha=1, color=color_list[i*4]))
        autolabel(rect_list[i],ax)
    
    ax.set_xticks([p + (1 - x_adj) * width for p in index])
    ax.set_xticklabels(namelist)
    plt.grid(axis='y')
    plt.legend(legend,bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0)
    ax.set_title(title1+' ('+filename.split('\\')[1]+')')
    ax.set_ylabel(y_label1)
    ax.set_xlabel(x_label1)
    plt.savefig(path+'\\'+file_name1, bbox_inches='tight')
    plt.close() # Disable ipython console plot
    #Figure 2
    plt.figure()
    fig, ax = plt.subplots(figsize=(10,5))
    width2 = (1 - 0.3)/len(namelist)
    index2 = np.arange(len(response_list))
    
    for i in range(0,len(namelist)):
        rect_list2.append(ax.bar([p + width2 * i for p in index2], df_list[i][1::], width2, alpha=1, color=color_list[-i*2]))
        autolabel(rect_list2[i],ax)
    
    ax.set_xticks([p + (len(namelist)/2 - 0.5) * width2 for p in index2])
    ax.set_xticklabels(legend)
    plt.grid(axis='y')
    plt.legend(namelist,bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0)
    ax.set_title(title2+' ('+filename.split('\\')[1]+')')
    ax.set_ylabel(y_label1)
    ax.set_xlabel(x_label2)
    plt.savefig(path+'\\'+file_name2, bbox_inches='tight')
    plt.close() # Disable ipython console plot
    

# Main
parameter_dict = get_parameter_dict() 
read_path = parameter_dict['temp.dir'].strip('./') + '\\' # temp\
output_path = parameter_dict['output.dir'].strip('./') # results\
file_format = ('*.csv')
file_list = glob.glob(read_path + file_format) #Full path will be "temp\*.csv" which gets a list of all .csv files in csv folder
for f in file_list:
    file_name = f.split('\\')[-1].split('.csv')[0]
    # Creates new path if it doesnt exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    save_path = output_path+'\\'+file_name+'_output'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    visualization(f,save_path)