#Output csv files will be saved into "\data\scraperesults\lowyat"

import scraper.crawler as c
import scraper.tlink_scraper as t
import scraper.post_scrape as p
import read_wordlist as wl
from ReadParameterFile import get_parameter_dict
import re

#List initialization
links_retrieved = []
titles = []
pd = get_parameter_dict()
save_dir = pd['lowyat.files'].strip('./')+'/'

#Read word list
search_list = wl.read_wordlist()

#************CONFIGURATION******************
#CRAWLER CONFIG
link = pd['scraper.c.link'] #Start link
levels = int(pd['scraper.c.levels']) #Currently limited to 2 levels
l1_search = pd['scraper.c.l1_search'].split(',') #Level 1 filter (/Kopitiam)
l2_search = pd['scraper.c.l2_search'].split(',') #Level 2 filter (/Kopitiam/SeriousKopitiam)

#THREAD LINK scraper CONFIG
page_limit = int(pd['scraper.t.page_limit']) #Default 50
#search_list = pd['scraper.t.search_list'].split(',')
start_date = pd['scraper.t.start_date'] #Format = %m/%d/%y
end_date = pd['scraper.t.end_date']

#POST scraper CONFIG
page_limit_p = int(pd['scraper.p.page_limit_p']) #Default 50
#************CONFIGURATION END******************

#CRAWLER
print ("[C] Crawler task started for " + str(levels) + " level(s) for keywords " + str(l1_search) + " at L1, " + str(l2_search) + " at L2.")
link_list = c.crawl_levels(link, levels, l1_search, l2_search)
print("[C] Crawler task completed")

#THREAD LINK scraper
print("\t[T] Link scraper initiated with keywords: " + str(search_list) + " With page limit: " + str(page_limit))
for l in link_list:
    print("\t[T] Link scraper task started for link: " + l)
    temp_retrieved, temp_titles, counter = t.tlink_scrape(l, page_limit, search_list, start_date, end_date)
    links_retrieved = links_retrieved + temp_retrieved
    titles = titles + temp_titles
print("\t[T] Link scraper retrieved links: " + str(links_retrieved))
print("\t[T] Link scraper task completed")
    
#POST scraper
count = 0
print("\t\t[P] Post scraper initiated with page limit: " + str(page_limit_p))
for l,ttl in zip(links_retrieved, titles):
    count += 1
    print("\t\t[P] Post scraper task started for link: " + str(l) + " (" + str(count) + "/" + str(len(links_retrieved)) + ")")
    df, counter = p.post_scrape(l, page_limit_p, counter)
    file_name = "lowyat_"+l.split("https://forum.lowyat.net/topic/")[1]+"_"+re.sub(r'[^\w]', ' ', ttl)
    df.to_csv(save_dir + file_name + ".csv", header=True, index=False)
print("\t\t[P] Post scraper task completed")