from AnalysisLib.ProcessFile import getObjectList, UpdateRecord, ProcessJsonData, ProcessFbData, ProcessMalaysiaKiniData, ProcessLowyatData, ProcessTweetData
from AnalysisLib.Scale import search_scale
from ReadParameterFile import get_parameter_dict
import threading

def definexYear(year, party_list, leader_list):
    leader_dict = {'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0],'13':[0,0],'14':[0,0],'15':[0,0],'16':[0,0],'17':[0,0],'18':[0,0],'19':[0,0],'20':[0,0],'21':[0,0],'22':[0,0],'23':[0,0],'24':[0,0],'25':[0,0],'26':[0,0],'27':[0,0],'28':[0,0],'29':[0,0],'30':[0,0],'31':[0,0]}
    xyear = {}
    for oyear in year:
        xyear[oyear] = {'01':{},'02':{},'03':{},'04':{},'05':{},'06':{},'07':{},'08':{}}
        
        for key, value in xyear[oyear].items():
            for party in party_list:
                    xyear[oyear][key][party.getName()] = leader_dict
            for leader in leader_list:
                    xyear[oyear][key][leader.getName()] = leader_dict
    #print(xyear)
    return xyear

def addScale(xyear, year, month, day, name, scale, _type):
    #party_dict = {'01':[0,0,0],'02':[0,0,0],'03':[0,0,0],'04':[0,0,0],'05':[0,0,0],'06':[0,0,0],'07':[0,0,0],'08':[0,0,0],'09':[0,0,0],'10':[0,0,0],'11':[0,0,0],'12':[0,0,0],'13':[0,0,0],'14':[0,0,0],'15':[0,0,0],'16':[0,0,0],'17':[0,0,0],'18':[0,0,0],'19':[0,0,0],'20':[0,0,0],'21':[0,0,0],'22':[0,0,0],'23':[0,0,0],'24':[0,0,0],'25':[0,0,0],'26':[0,0,0],'27':[0,0,0],'28':[0,0,0],'29':[0,0,0],'30':[0,0,0],'31':[0,0,0]}
    #policy_dict = {'01':[0,0,0,0,0],'02':[0,0,0,0,0],'03':[0,0,0,0,0],'04':[0,0,0,0,0],'05':[0,0,0,0,0],'06':[0,0,0,0,0],'07':[0,0,0,0,0],'08':[0,0,0,0,0],'09':[0,0,0,0,0],'10':[0,0,0,0,0],'11':[0,0,0,0,0],'12':[0,0,0,0,0],'13':[0,0,0,0,0],'14':[0,0,0,0,0],'15':[0,0,0,0,0],'16':[0,0,0,0,0],'17':[0,0,0,0,0],'18':[0,0,0,0,0],'19':[0,0,0,0,0],'20':[0,0,0,0,0],'21':[0,0,0,0,0],'22':[0,0,0,0,0],'23':[0,0,0,0,0],'24':[0,0,0,0,0],'25':[0,0,0,0,0],'26':[0,0,0,0,0],'27':[0,0,0,0,0],'28':[0,0,0,0,0],'29':[0,0,0,0,0],'30':[0,0,0,0,0],'31':[0,0,0,0,0]}
    #select_dict = {'party':party_dict, 'leader':leader_dict, 'policy':policy_dict}

    if year in xyear:
    #if month in xyear[year]:
        xyear[year][month][name][day][scale] += 1
     #   else:
      #      leader_dict = {'01':[0,0],'02':[0,0],'03':[0,0],'04':[0,0],'05':[0,0],'06':[0,0],'07':[0,0],'08':[0,0],'09':[0,0],'10':[0,0],'11':[0,0],'12':[0,0],'13':[0,0],'14':[0,0],'15':[0,0],'16':[0,0],'17':[0,0],'18':[0,0],'19':[0,0],'20':[0,0],'21':[0,0],'22':[0,0],'23':[0,0],'24':[0,0],'25':[0,0],'26':[0,0],'27':[0,0],'28':[0,0],'29':[0,0],'30':[0,0],'31':[0,0]}
       #     xyear[year][month][name] = leader_dict
        #    xyear[year][month][name][day][scale] += 1
    return xyear

def compute(word):
    global yearTable
    print(word)
    word[0] = word[0].lower()
    mutex.acquire()
    for party in party_list: #search if any party name in the sentence
        if party.getName() in word[0]: # if sentence contains words found in scale database
            #attitude likert scale
            if search_scale("Attitude",1,word[0]): # search whether this word in database
                yearTable = addScale(yearTable, word[3], word[2], word[1], party.getName(), 0, "party")
            elif search_scale("Attitude",3,word[0]):
                yearTable = addScale(yearTable, word[3], word[2], word[1], party.getName(), 1, "party")
       
    #for govtPolicy in govtPolicy_list: 
    #    if govtPolicy.getName() in word[0]: 
    #        #perception likert scale
    #        if search_scale("Perception",1,word[0]): 
    #            yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 0, "policy")
    #        elif search_scale("Perception",2,word[0]):
    #            yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 1, "policy")
    
    for leader in leader_list: 
        if leader.getName() in word[0]: 
            #popularity likert scale
            if search_scale("Popularity", 1, word[0]):
                yearTable = addScale(yearTable, word[3], word[2], word[1], leader.getName(), 0, "leader")
            elif search_scale("Popularity", 5, word[0]):
                yearTable = addScale(yearTable, word[3], word[2], word[1], leader.getName(), 1, "leader")
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
    return yearTable

##main program
mutex = threading.Lock()

param = get_parameter_dict()

party_list = getObjectList("Party", param["target"] + '/party.txt')
#govtPolicy_list = getObjectList("GovtPolicy", param["target"] + '/govtPolicy.txt')
leader_list = getObjectList("Leader", param["target"] + '/leader.txt')

full_word_list = []
#word_list += ProcessJsonData(param["json.files"])
#word_list += ProcessFbData(param["facebook.files"])
#word_list += ProcessMalaysiaKiniData(param["malaysiakini.files"])
full_word_list += ProcessLowyatData(param["lowyat.files"])

yearTable = definexYear(['17'], party_list, leader_list)

while(len(full_word_list) >= 10):
    print(len(full_word_list))
    xxx = full_word_list[:10]
    full_word_list = full_word_list[10:]
    getResult(xxx)
    #del xxx
getResult(full_word_list)

UpdateRecord(param['temp.dir'], yearTable)
#print(tt)
#_location = getDirInTemp(param["temp.dir"])
