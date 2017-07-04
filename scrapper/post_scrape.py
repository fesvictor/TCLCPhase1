import urllib
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

global page_no
global counter
page_no = 0
counter = 0

def post_scrape_main(link):
    main_link = "https://forum.lowyat.net"
    try:
        page = urllib.request.urlopen(link)
    except:
        return 0
    
    soup = bs(page, "lxml")
    #For debugging purposes, prints raw html to file
#    with open('temp.html', 'wb') as f:
#        f.write(soup.prettify('utf8'))
    
    [div.extract() for div in soup.find_all("div", { "class" : "quotemain"})]   #Removes quote text
    [div.extract() for div in soup.find_all("div", { "class" : "quotetop"})]    #Removes quote timestamp
    [div.extract() for div in soup.find_all("span", { "class" : "edit"})]       #Removes edit text and timestamps
    
    un_list = []
    time_list = []
    avatar_title = []
    info_group = []
    info_post_count = []
    info_joined = []
    info_from = []
    text = []
    
    usernames = soup.find_all("span", class_="normalname")
    for a in usernames:
        un_list.append(a.get_text())
        
    timestamp = soup.find_all("div", style="float: left;")
    for a in timestamp:
        try:
            time_list.append(a.find('span', class_='postdetails').get_text())
        except:
            pass
    
    userinfo = soup.find_all("table", class_="post_table")
    for a in userinfo:
        avatar_title.append(a.find("div", class_="avatar").get_text().strip())
        info_group.append(list(a.find("div", class_="avatar_extra").stripped_strings)[0])
        info_post_count.append(list(a.find("div", class_="avatar_extra").stripped_strings)[1])
        info_joined.append(list(a.find("div", class_="avatar_extra").stripped_strings)[2])
        try:
            info_from.append(list(a.find("div", class_="avatar_extra").stripped_strings)[3])
        except IndexError:
            info_from.append("")
        try:
            text.append(a.find("div", class_="postcolor post_text").get_text().strip())
        except:
            text.append("")
    try:
        np_link = main_link + soup.find("a", title="Next page")['href']
    except:
        np_link = 0
    
    index_set = list(zip(un_list,time_list,avatar_title,info_group,info_post_count,info_joined,info_from,text))
    df = pd.DataFrame(data = index_set, columns=['username','time','avatar_title','group','post_count','join_date','from','text'])
    return df, np_link

def post_scrape(link, page_limit=50):
    global page_no
    global counter
    page_no = 0
    frames = []
    
    while (True):
        if (counter == 45):
            print("\t\t[P] *****15 second delay initated to prevent forum block*****")
            time.sleep(15)
            counter = 0
        if (page_no == page_limit):
            return pd.concat(frames, ignore_index=True)
        page_no += 1
        counter += 1
        if page_no == 1:
            print("\t\t[P] Page = " + str(page_no) + " Counter = " + str(counter) + " " + link)
            prev_link = link
            df, np_link = post_scrape_main(link)
            frames.append(df)
            if np_link == 0:
                print("\t\t[P] Last page reached at: " + prev_link)
                return pd.concat(frames, ignore_index=True)
        else:
            print("\t\t[P] Page = " + str(page_no) + " Counter = " + str(counter) + " " + np_link)
            prev_link = np_link
            df, np_link = post_scrape_main(np_link)
            frames.append(df)
            if np_link == 0:
                print("\t\t[P] Last page reached at: " + prev_link)
                return pd.concat(frames, ignore_index=True)
    