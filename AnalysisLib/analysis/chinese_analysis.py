import os
os.chdir('C:/Users/tanhongzher/Documents/GitHub')

from TCLCPhase1.AnalysisLib.Scale import search_scale
#from TCLCPhase1.AnalysisLib.analysis.compute import compute 
from TCLCPhase1.AnalysisLib.analysis.get_year_table import get_year_table
#from TCLCPhase1.AnalysisLib.analysis.get_result import get_result
from TCLCPhase1.AnalysisLib.process_file.get_object_list import get_object_list
from TCLCPhase1.AnalysisLib.process_file.process_fb_data import process_fb_data
from TCLCPhase1.AnalysisLib.process_file.process_json_data import process_json_data
from TCLCPhase1.AnalysisLib.process_file.process_lowyat_data import process_lowyat_data
from TCLCPhase1.AnalysisLib.process_file.process_malaysia_kini_data import process_malaysia_kini_data
from TCLCPhase1.AnalysisLib.process_file.process_tweet_data import process_tweet_data
from TCLCPhase1.AnalysisLib.process_file.process_cari_data import process_cari_data
from TCLCPhase1.AnalysisLib.process_file.process_jbtalks_data import process_jbtalks_data
from TCLCPhase1.AnalysisLib.process_file.update_result import update_result

from TCLCPhase1.get_parameter_dict import get_parameter_dict
from time import time
import threading

def definexYear(year, party_list, leader_list):
    #leader_dict = {'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0],'13':[0,0],'14':[0,0],'15':[0,0],'16':[0,0],'17':[0,0],'18':[0,0],'19':[0,0],'20':[0,0],'21':[0,0],'22':[0,0],'23':[0,0],'24':[0,0],'25':[0,0],'26':[0,0],'27':[0,0],'28':[0,0],'29':[0,0],'30':[0,0],'31':[0,0]}
    xyear = {}
    for oyear in year:
        xyear[oyear] = {'01':{},'02':{},'03':{},'04':{},'05':{},'06':{},'07':{},'08':{} , '09':{}, '10':{},'11':{}, '12':{}}
        
        for key, value in xyear[oyear].items():
            xyear[oyear][key]['party'] = {}
            for party in party_list:
                    xyear[oyear][key]['party'][party.get_name()[0]] = {'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0],'13':[0,0],'14':[0,0],'15':[0,0],'16':[0,0],'17':[0,0],'18':[0,0],'19':[0,0],'20':[0,0],'21':[0,0],'22':[0,0],'23':[0,0],'24':[0,0],'25':[0,0],'26':[0,0],'27':[0,0],'28':[0,0],'29':[0,0],'30':[0,0],'31':[0,0]}
            xyear[oyear][key]['leader'] = {}
            for leader in leader_list:
                    xyear[oyear][key]['leader'][leader.get_name()[0]] = {'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0],'13':[0,0],'14':[0,0],'15':[0,0],'16':[0,0],'17':[0,0],'18':[0,0],'19':[0,0],'20':[0,0],'21':[0,0],'22':[0,0],'23':[0,0],'24':[0,0],'25':[0,0],'26':[0,0],'27':[0,0],'28':[0,0],'29':[0,0],'30':[0,0],'31':[0,0]}
    #print(xyear)
    return xyear

def addScale(year, month, day, name, scale, _type):
    global yearTable
    #party_dict = {'01':[0,0,0],'02':[0,0,0],'03':[0,0,0],'04':[0,0,0],'05':[0,0,0],'06':[0,0,0],'07':[0,0,0],'08':[0,0,0],'09':[0,0,0],'10':[0,0,0],'11':[0,0,0],'12':[0,0,0],'13':[0,0,0],'14':[0,0,0],'15':[0,0,0],'16':[0,0,0],'17':[0,0,0],'18':[0,0,0],'19':[0,0,0],'20':[0,0,0],'21':[0,0,0],'22':[0,0,0],'23':[0,0,0],'24':[0,0,0],'25':[0,0,0],'26':[0,0,0],'27':[0,0,0],'28':[0,0,0],'29':[0,0,0],'30':[0,0,0],'31':[0,0,0]}
    #policy_dict = {'01':[0,0,0,0,0],'02':[0,0,0,0,0],'03':[0,0,0,0,0],'04':[0,0,0,0,0],'05':[0,0,0,0,0],'06':[0,0,0,0,0],'07':[0,0,0,0,0],'08':[0,0,0,0,0],'09':[0,0,0,0,0],'10':[0,0,0,0,0],'11':[0,0,0,0,0],'12':[0,0,0,0,0],'13':[0,0,0,0,0],'14':[0,0,0,0,0],'15':[0,0,0,0,0],'16':[0,0,0,0,0],'17':[0,0,0,0,0],'18':[0,0,0,0,0],'19':[0,0,0,0,0],'20':[0,0,0,0,0],'21':[0,0,0,0,0],'22':[0,0,0,0,0],'23':[0,0,0,0,0],'24':[0,0,0,0,0],'25':[0,0,0,0,0],'26':[0,0,0,0,0],'27':[0,0,0,0,0],'28':[0,0,0,0,0],'29':[0,0,0,0,0],'30':[0,0,0,0,0],'31':[0,0,0,0,0]}
    #select_dict = {'party':party_dict, 'leader':leader_dict, 'policy':policy_dict}
    
    if year in yearTable:
    #if month in xyear[year]:
        yearTable[year][month][_type][name][day][scale] += 1
     #   else:
      #      leader_dict = {'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0],'13':[0,0],'14':[0,0],'15':[0,0],'16':[0,0],'17':[0,0],'18':[0,0],'19':[0,0],'20':[0,0],'21':[0,0],'22':[0,0],'23':[0,0],'24':[0,0],'25':[0,0],'26':[0,0],'27':[0,0],'28':[0,0],'29':[0,0],'30':[0,0],'31':[0,0]}
       #     xyear[year][month][name] = leader_dict
        #    xyear[year][month][name][day][scale] += 1
        
def get_result(word_list):
    #word_list += process_tweet_data(param["twitter.files"])
    threads = []
    for word in word_list:  #process every sentence
        threads.append(threading.Thread(target=compute, args=(word,)) )
    for t in threads:
        t.start() 
    for t in threads: #[t.join() for t in threads] don't work
        t.join()
        
    del threads
    del word_list
    #return yearTable
  
def compute(word):
    #print(word)
    global i
    global yearTable
    word[0] = word[0].lower()
    mutex.acquire()
    for party in party_list: #search if any party name in the sentence
        for party_name in party.get_name():
            if party_name in word[0]: # if sentence contains words found in scale database
                #attitude likert scale
                if search_scale('Polarity', 1, word[0], 'chinese'): # search whether this word in database
                    i += 1
                    addScale(word[3], word[2], word[1], party.get_name()[0], 0, 'party')
                    break
                elif search_scale('Polarity', 2, word[0], 'chinese'):
                    i += 1
                    addScale(word[3], word[2], word[1], party.get_name()[0], 1, 'party')
                    break
       
    #for govtPolicy in govtPolicy_list: 
    #    if govtPolicy.getName() in word[0]: 
    #        #perception likert scale
    #        if search_scale("Perception",1,word[0]): 
    #            yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 0, "policy")
    #        elif search_scale("Perception",2,word[0]):
    #            yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 1, "policy")
    
    for leader in leader_list:
        for leader_name in leader.get_name():
            if leader_name in word[0]: 
                #popularity likert scale
                if search_scale('Polarity', 1, word[0], 'chinese'):
                    i += 1
                    addScale(word[3], word[2], word[1], leader.get_name()[0], 0, 'leader')
                    break
                elif search_scale('Polarity', 2, word[0], 'chinese'):
                    i += 1
                    addScale(word[3], word[2], word[1], leader.get_name()[0], 1, 'leader')
                    break
    mutex.release()

   
##main program 
mutex = threading.Lock() 

param = get_parameter_dict() 

party_list = get_object_list('party', param['target'] + '/chinese_party.txt', 'chinese')
#govtPolicy_list = getObjectList("GovtPolicy", param["target"] + '/govtPolicy.txt')
leader_list = get_object_list('leader', param['target'] + '/chinese_leader.txt', 'chinese')

#if not os.path.exists("./temp"): 
#    os.makedirs("./temp") 

t0 = time()

i = 0
others_list = []
others_list += process_jbtalks_data('TCLCPhase1/' + param['jbtalks.files'])
others_list += process_cari_data('TCLCPhase1/' + param['carinet.files'])
#location of carinet: /data/scraperesults/carinet

print(others_list)

yearTable = definexYear(['17'], party_list, leader_list) 

while(len(others_list) >= 10): 
    print('the remaining: ', len(others_list)) 
    xxx = others_list[:10] 
    others_list = others_list[10:] 
    get_result(xxx) 
print(len(others_list))
get_result(others_list)    
    
update_result(['17'], 12, 'TCLCPhase1/' + param['temp.chinese.others.dir'], yearTable , 'others' , 'chinese') 

print("total scale count from others:", i) 

print("total time taken:", time() - t0, " seconds")