#Output csv files will be saved into "\data\scraperesults\lowyat"

import scrapper.crawler as c
import scrapper.tlink_scraper as t
import scrapper.post_scrape as p
from ReadParameterFile import get_parameter_dict
import re

#List initialization
links_retrieved = []
titles = []
parameter_dict = get_parameter_dict()
save_dir = parameter_dict['lowyat.files'].strip('./')+'/'

#************CONFIGURATION******************
#CRAWLER CONFIG
link = "https://forum.lowyat.net/" #Start link
levels = 2 #Currently limited to 2 levels
l1_search = ["Kopi"] #Level 1 filter (/Kopitiam)
l2_search = ["serious"] #Level 2 filter (/Kopitiam/SeriousKopitiam)

#THREAD LINK SCRAPPER CONFIG
page_limit = 1 #Default 50
search_list = ["DAP","malaysia"]

#POST SCRAPPER CONFIG
page_limit_p = 10 #Default 50
#************CONFIGURATION END******************

#CRAWLER
print ("[C] Crawler task started for " + str(levels) + " level(s) for keywords " + str(l1_search) + " at L1, " + str(l2_search) + " at L2.")
link_list = c.crawl_levels(link, levels, l1_search, l2_search)
print("[C] Crawler task completed")

#THREAD LINK SCRAPPER
print("\t[T] Link scrapper initiated with keywords: " + str(search_list))
for l in link_list:
    print("\t[T] Link scrapper task started for link: " + l)
    temp_retrieved, temp_titles = t.tlink_scrape(l, page_limit, search_list)
    links_retrieved = links_retrieved + temp_retrieved
    titles = titles + temp_titles
print("\t[T] Link scrapper retrieved links: " + str(links_retrieved))
print("\t[T] Link scrapper task completed")
    
#POST SCRAPPER
count = 0
for l,ttl in zip(links_retrieved, titles):
    count += 1
    print("\t\t[P] Post scrapper task started for link: " + str(l) + " (" + str(count) + "/" + str(len(links_retrieved)) + ")")
    df = p.post_scrape(l, page_limit_p)
    file_name = "lowyat_"+l.split("https://forum.lowyat.net/topic/")[1]+"_"+re.sub(r'[^\w]', ' ', ttl)
    df.to_csv(save_dir + file_name + ".csv", header=True, index=False)
print("\t\t[P] Post scrapper task completed")