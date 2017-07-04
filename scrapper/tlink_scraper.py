import urllib
from bs4 import BeautifulSoup as bs
import time
#import pandas as pd

global page_no
global counter
page_no = 0
counter = 0

def tlink_scrape_main(link, search_list=[]):
    main_link = "https://forum.lowyat.net"
    page = urllib.request.urlopen(link)
    soup = bs(page, "lxml")
    
    #For debugging purposes, prints raw html to file
#    with open('temp.html', 'wb') as f:
#        f.write(soup.prettify('utf8'))
    
    titles = []
    desc = []
    tlink = []
    
    topics = soup.find_all("td", class_="row1", valign="middle")
    
    for a in topics:
        if search_list != []:
            for word in search_list:
                try:
                    if (word.lower() in list(a.stripped_strings)[0].lower()) or (word.lower() in list(a.stripped_strings)[5].lower()):
                        titles.append(list(a.stripped_strings)[0])
                        try:
                            desc.append(list(a.stripped_strings)[5])
                        except:
                            desc.append("")
                        tlink.append(main_link + a.find("a")['href'])
                except:
                    if word.lower() in list(a.stripped_strings)[0].lower():
                        titles.append(list(a.stripped_strings)[0])
                        try:
                            desc.append(list(a.stripped_strings)[5])
                        except:
                            desc.append("")
                        tlink.append(main_link + a.find("a")['href'])
        else:
            titles.append(list(a.stripped_strings)[0])
            try:
                desc.append(list(a.stripped_strings)[5])
            except:
                desc.append("")
            tlink.append(main_link + a.find("a")['href'])
    try:
        np_link = main_link + soup.find("a", title="Next page")['href']
    except:
        np_link = 0
    
#    index_set = list(zip(titles,desc,tlink))
#    df = pd.DataFrame(data = index_set, columns=['titles','desc','link'])
#    df.to_csv('temp.csv',index=False)
    
    return tlink, np_link, titles

def tlink_scrape(link, page_limit=50, search_list=[]):
    global page_no
    global counter
    page_no = 0
    links_retrieved = []
    titles = []
    
    while (True):
        if (counter == 45):
            print("\t[T] *****15 second delay initated to prevent forum block*****")
            time.sleep(15)
            counter = 0
        if (page_no == page_limit):
            return links_retrieved, titles
        page_no += 1
        counter += 1
        if page_no == 1:
            print("\t[T] Page = " + str(page_no) + " Counter = " + str(counter) + " " + link)
            prev_link = link
            tlink, np_link, titles = tlink_scrape_main(link, search_list)
            links_retrieved = links_retrieved + tlink
            if np_link == 0:
                print("\tLast page reached at: " + prev_link)
                return links_retrieved, titles
        else:
            print("\t[T] Page = " + str(page_no) + " Counter = " + str(counter) + " " + np_link)
            prev_link = np_link
            tlink, np_link, titles = tlink_scrape_main(np_link, search_list)
            links_retrieved = links_retrieved + tlink
            if np_link == 0:
                print("\t[T] Last page reached at: " + prev_link)
                return links_retrieved, titles