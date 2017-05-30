import csv
import matplotlib.pyplot as plt
import numpy as np

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

n_groups = len(inputdict)
index = np.arange (n_groups)
width = 0.25

plt.figure(1)
fig, ax = plt.subplots(figsize=(10,5))

rect1 = ax.bar(index, oppose_list, width, alpha=0.5, color='r')
rect2 = ax.bar([p + width for p in index], notsure_list, width, alpha=0.5, color='g')
rect3 = ax.bar([p + width*2 for p in index], consent_list, width, alpha=0.5, color='b')

ax.set_xticks([p + 1 * width for p in index])
ax.set_xticklabels(partylist)
plt.ylim([0, max(inputdict['BN'] + inputdict['DAP'] + inputdict['PKR'])+20])
plt.grid()
plt.legend(['Oppose','Not Sure', 'Consent'],loc='upper left')
ax.set_title('Grouped by Party')
ax.set_ylabel('Count')
ax.set_xlabel('Party')

autolabel(rect1)
autolabel(rect2)
autolabel(rect3)

plt.savefig('party_plot.png')

plt.figure(2)
fig, ax = plt.subplots(figsize=(10,5))

rect4 = ax.bar(index, inputdict['BN'], width, alpha=0.8, color='C0')
rect5 = ax.bar([p + width for p in index], inputdict['DAP'], width, alpha=0.8, color='C1')
rect6 = ax.bar([p + width*2 for p in index], inputdict['PKR'], width, alpha=0.8, color='C2')

ax.set_xticks([p + 1 * width for p in index])
ax.set_xticklabels(['Oppose','Not Sure','Consent'])
plt.ylim([0, max(oppose_list + notsure_list + consent_list)+20])
plt.grid()
plt.legend(partylist,loc='upper left')
ax.set_title('Grouped by Response')
ax.set_ylabel('Count')
ax.set_xlabel('Response')

autolabel(rect4)
autolabel(rect5)
autolabel(rect6)

plt.savefig('response_plot.png')

plt.show()