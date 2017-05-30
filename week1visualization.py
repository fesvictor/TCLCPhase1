import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height), ha='center', va='bottom')

csvfile = open('recordss.csv',"r")
reader = csv.reader(csvfile)

header = next(reader) #Stores first line as header
inputdict = {}
partylist = []
oppose_list = []
notsure_list = []
consent_list = []
response_list = []
rect_list = []
rect_list2 = []
color_list = ['b','g','r','c','m','y','k']

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
    rect_list.append(ax.bar([p + width*i for p in index], response_list[i], width, alpha=0.7, color=color_list[i]))
    autolabel(rect_list[i])

ax.set_xticks([p + 1 * width for p in index])
ax.set_xticklabels(partylist)
plt.ylim([0, max(inputdict['BN'] + inputdict['DAP'] + inputdict['PKR'])+20])
plt.grid()
plt.legend(['Oppose','Not Sure', 'Consent'],loc='upper left')
ax.set_title('Grouped by Party')
ax.set_ylabel('Count')
ax.set_xlabel('Party')

plt.savefig('party_plot.png')

plt.figure(2)
fig, ax = plt.subplots(figsize=(10,5))

print (df_list)
print (response_list)

width2 = 0.12
index2 = np.arange(len(response_list))

for i in range(0,len(partylist)):
    rect_list2.append(ax.bar([p + width2 * i for p in index2], df_list[i][1::], width2, alpha=0.7, color=color_list[-i]))
    print (df_list[i][1::])
    autolabel(rect_list2[i])

ax.set_xticks([p + (len(partylist)/2 - 0.5) * width2 for p in index2])
ax.set_xticklabels(['Oppose','Not Sure','Consent'])
plt.ylim([0, max(oppose_list + notsure_list + consent_list)+30])
plt.grid()
plt.legend(partylist,loc='upper left')
ax.set_title('Grouped by Response')
ax.set_ylabel('Count')
ax.set_xlabel('Response')

plt.savefig('response_plot.png')

plt.show()