from AnalysisLib.ProcessFile import getObjectList, UpdateResult, ProcessJsonData, ProcessFbData, ProcessMalaysiaKiniData, ProcessLowyatData, ProcessTweetData, ProcessCariData, ProcessJbtalksData
from AnalysisLib.Scale import search_scale
from ReadParameterFile import get_parameter_dict
from time import time
import threading

def definexYear(year, party_list, leader_list):
    #leader_dict = {'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0],'13':[0,0],'14':[0,0],'15':[0,0],'16':[0,0],'17':[0,0],'18':[0,0],'19':[0,0],'20':[0,0],'21':[0,0],'22':[0,0],'23':[0,0],'24':[0,0],'25':[0,0],'26':[0,0],'27':[0,0],'28':[0,0],'29':[0,0],'30':[0,0],'31':[0,0]}
    xyear = {}
    for oyear in year:
        xyear[oyear] = {'01':{},'02':{},'03':{},'04':{},'05':{},'06':{},'07':{},'08':{} , '09':{}, '10':{},'11':{} ,'12' :{}}
        
        for key, value in xyear[oyear].items():
            xyear[oyear][key]['party'] = {}
            for party in party_list:
                    xyear[oyear][key]['party'][party.getName()[0]] = {'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0],'13':[0,0],'14':[0,0],'15':[0,0],'16':[0,0],'17':[0,0],'18':[0,0],'19':[0,0],'20':[0,0],'21':[0,0],'22':[0,0],'23':[0,0],'24':[0,0],'25':[0,0],'26':[0,0],'27':[0,0],'28':[0,0],'29':[0,0],'30':[0,0],'31':[0,0]}
            xyear[oyear][key]['leader'] = {}
            for leader in leader_list:
                    xyear[oyear][key]['leader'][leader.getName()[0]] = {'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0],'13':[0,0],'14':[0,0],'15':[0,0],'16':[0,0],'17':[0,0],'18':[0,0],'19':[0,0],'20':[0,0],'21':[0,0],'22':[0,0],'23':[0,0],'24':[0,0],'25':[0,0],'26':[0,0],'27':[0,0],'28':[0,0],'29':[0,0],'30':[0,0],'31':[0,0]}
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

def compute(word):
    #print(word)
    global i
    global yearTable
    word[0] = word[0].lower()
    mutex.acquire()
    for party in party_list: #search if any party name in the sentence
        for party_name in party.getName():
            if party_name in word[0]: # if sentence contains words found in scale database
                #attitude likert scale
                if search_scale('Polarity', 1, word[0], 'chinese'): # search whether this word in database
                    i += 1
                    addScale(word[3], word[2], word[1], party.getName()[0], 0, 'party')
                    break
                elif search_scale('Polarity', 2, word[0], 'chinese'):
                    i += 1
                    addScale(word[3], word[2], word[1], party.getName()[0], 1, 'party')
                    break
       
    #for govtPolicy in govtPolicy_list: 
    #    if govtPolicy.getName() in word[0]: 
    #        #perception likert scale
    #        if search_scale("Perception",1,word[0]): 
    #            yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 0, "policy")
    #        elif search_scale("Perception",2,word[0]):
    #            yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 1, "policy")
    
    for leader in leader_list:
        for leader_name in leader.getName():
            if leader_name in word[0]: 
                #popularity likert scale
                if search_scale('Polarity', 1, word[0], 'chinese'):
                    i += 1
                    addScale(word[3], word[2], word[1], leader.getName()[0], 0, 'leader')
                    break
                elif search_scale('Polarity', 2, word[0], 'chinese'):
                    i += 1
                    addScale(word[3], word[2], word[1], leader.getName()[0], 1, 'leader')
                    break
    mutex.release()

def getResult(word_list):
    #word_list += ProcessTweetData(param["twitter.files"])
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

##main program
mutex = threading.Lock()

param = get_parameter_dict()

party_list = getObjectList('Party', param['target'] + '/chinese_party.txt', 'chinese')
#govtPolicy_list = getObjectList("GovtPolicy", param["target"] + '/govtPolicy.txt')
leader_list = getObjectList('Leader', param['target'] + '/chinese_leader.txt', 'chinese')

#if not os.path.exists("./temp"):
#    os.makedirs("./temp")

t0 = time()

i = 0
'''
fb_list = ProcessFbData(param['facebook.files'])
yearTable = definexYear(['17'], party_list, leader_list)
while(len(fb_list) >= 10):
    #print(len(fb_list))
    xxx = fb_list[:10]
    fb_list = fb_list[10:]
    getResult(xxx)
UpdateResult(['17'], 12, param['temp.chinese.facebook.dir'], yearTable, 'facebook', 'chinese')
print("total scale count from facebook:", i)
'''

'''
i = 0
tweet_list = ProcessTweetData(param['twitter.files'])
yearTable = definexYear(['17'], party_list, leader_list)

while(len(tweet_list) >= 5):
    #print(len(tweet_list))
    xxx = tweet_list[:5]
    tweet_list = tweet_list[5:]
    getResult(xxx)
UpdateResult(['17'], 12, param['temp.chinese.tweet.dir'], yearTable, 'twitter', 'chinese')
print("total scale count from twitter:", i)
'''

i = 0
others_list = []
others_list += ProcessJbtalksData(param['jbtalks.files'])
others_list += ProcessCariData(param['carinet.files'])
#location of carinet: /data/scraperesults/carinet

print(others_list)

yearTable = definexYear(['17'], party_list, leader_list) 
while(len(others_list) >= 10): 
    print('the remaining: ', len(others_list)) 
    xxx = others_list[:10] 
    others_list = others_list[10:] 
    getResult(xxx) 
    
UpdateResult(['17'], 12, param['temp.chinese.others.dir'], yearTable , 'others' , 'chinese') 

print("total scale count from others:", i) 

print("total time taken:", time() - t0, " seconds") 