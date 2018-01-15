from TCLCPhase1.AnalysisLib.Scale import search_scale
from TCLCPhase1.AnalysisLib.analysis.compute import compute 
from TCLCPhase1.AnalysisLib.analysis.get_year_table import get_year_table
from TCLCPhase1.AnalysisLib.analysis.get_result import get_result
from TCLCPhase1.AnalysisLib.process_file.get_object_list import get_object_list
from TCLCPhase1.AnalysisLib.process_file.process_fb_data import process_fb_data
from TCLCPhase1.AnalysisLib.process_file.process_json_data import process_json_data
from TCLCPhase1.AnalysisLib.process_file.process_lowyat_data import process_lowyat_data
from TCLCPhase1.AnalysisLib.process_file.process_malaysia_kini_data import process_malaysia_kini_data
from TCLCPhase1.AnalysisLib.process_file.process_tweet_data import process_tweet_data
from TCLCPhase1.AnalysisLib.process_file.update_result import update_result

from TCLCPhase1.get_parameter_dict import get_parameter_dict
from time import time
import threading





##main program
mutex = threading.Lock()

param = get_parameter_dict()

party_list = get_object_list("party")
#govtPolicy_list = get_object_list("GovtPolicy", param["target"] + '/govtPolicy.txt')
leader_list = get_object_list("leader")

t0 = time()
i = 0
others_list = []
others_list += process_json_data(param["json.files"])
others_list += process_malaysia_kini_data(param["malaysiakini.files"])
others_list += process_lowyat_data(param["lowyat.files"])
yearTable = get_year_table(['17'], party_list, leader_list)


"""
The following section is to limit the thread number to 10 at once.
This is because by default threads will be created as much as possible 
which will eventually raise an error
"""
while(len(others_list) >= 10):
    #print(len(others_list))
    xxx = others_list[:10]
    others_list = others_list[10:]
    get_result(xxx)



update_result(param['temp.others.dir'], yearTable , 'others_')
print("total scale count from others:", i)
i = 0
fb_list = process_fb_data(param["facebook.files"])
yearTable = get_year_table(['17'], party_list, leader_list)
while(len(fb_list) >= 10):
    #print(len(fb_list))
    xxx = fb_list[:10]
    fb_list = fb_list[10:]
    get_result(xxx)
update_result(param['temp.facebook.dir'], yearTable, 'facebook_')
print("total scale count from facebook:", i)

i = 0
tweet_list = process_tweet_data(param['twitter.files'])
yearTable = get_year_table(['17'], party_list, leader_list)

while(len(tweet_list) >= 5):
    #print(len(tweet_list))
    xxx = tweet_list[:5]
    tweet_list = tweet_list[5:]
    get_result(xxx)
update_result(param['temp.tweet.dir'], yearTable, 'twitter_')
print("total scale count from twitter:", i)
print(time() - t0)