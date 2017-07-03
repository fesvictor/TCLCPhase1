import urllib
from bs4 import BeautifulSoup as bs
#import pandas as pd
import time

global page_no
global counter
global saved_link
saved_link = []
page_no = 0
counter = 0

def thread_links_scrape(link, page_limit=50, search_list=[], first_time=True):
    global page_no
    global counter
    global original_link
    if (page_no==0): original_link = link

    page_no += 1
    counter += 1
    print ("Page = " + str(page_no) + " Counter = " + str(counter) + " " + link)
    page = urllib.request.urlopen(link)
    soup = bs(page, "lxml")
    
    #For debugging purposes, prints raw html to file
#    with open('level2_raw_html.html', 'wb') as f:
#        f.write(soup.prettify('utf8'))
    
    #Store next page link
    try:
        next_page = soup.find("a", title="Next page")['href'].split("/")[-1]
    except:
        next_page = []
    next_page_link = original_link + "/" + next_page
    td = soup.find_all("td", class_="row1", valign="middle")
    
    title = []
    time_ = []
    page_ = []

    for a in td:
        raw = a.find("a")
        title.append(raw.get_text().strip().encode("ascii", 'ignore').decode("ascii", 'ignore'))
        time_.append(raw['title'][24:])
        #saved_link.append(original_link+raw['href'])
        page_.append(page_no)
    saved_link.append(next_page_link)
#    index_set = list(zip(title,time_,page_,saved_link))
#    csv_file = "level2_kopitiam.csv"
#    if first_time == True:
#        df = pd.DataFrame(data=index_set, columns=["title","time","page no","link"])
#        df.to_csv(csv_file,index=False)
#    else:
#        df = pd.DataFrame(data=index_set)
#        with open(csv_file,'a') as csv:
#            df.to_csv(csv, header=False, index=False)
    
    if counter == 45:
        time.sleep(15)
        counter = 0
    
    if page_no == page_limit:
        return saved_link
    
    #Check for next page
    if next_page != []:
        thread_links_scrape(next_page_link, page_limit, search_list, first_time=False)
        
print(thread_links_scrape("https://forum.lowyat.net/Kopitiam", page_limit=5))