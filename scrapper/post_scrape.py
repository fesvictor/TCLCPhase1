import urllib
from bs4 import BeautifulSoup as bs
import pandas as pd

def post_scrape(link):
    try:
        page = urllib.request.urlopen(link)
    except:
        return
    
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
    
    

    index_set = list(zip(un_list,time_list,avatar_title,info_group,info_post_count,info_joined,info_from,text))
    df = pd.DataFrame(data = index_set, columns=['username','time','avatar_title','group','post_count','join_date','from','text'])
    return df
