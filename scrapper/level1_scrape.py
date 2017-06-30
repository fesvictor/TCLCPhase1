import urllib
from bs4 import BeautifulSoup as bs
import pandas as pd
import pprint

def level1_scrape(link, search_list):
    page = urllib.request.urlopen(link)
    soup = bs(page, "lxml")
    
    #For debugging purposes, prints raw html to file
#    with open('level1_raw_html.html', 'wb') as f:
#        f.write(soup.prettify('utf8'))
    
    [div.extract() for div in soup.find_all("td", { "align" : "center"})]
    soup.find("div", id="fo_stat").decompose()
    td = soup.find_all("td", class_="row2")
    href = []
    title = []
    result_list = []
    for b in td:
        href.append(link[:-1]+b.find("b").findNext("a")['href']) #Reconstruct link from href
        title.append(b.find("b").findNext("a").get_text())
        
    index_set = list(zip(title,href))
    l1_df = pd.DataFrame(data = index_set, columns=['Topic','href'])
    l1_df.to_csv('level1.csv',index=False)
    #Pretty Print List
    pp = pprint.PrettyPrinter(width=200)
    pp.pprint(index_set)
    
    for i in range(0,len(index_set)):
        for word in search_list:
            if word in index_set[i][0].lower():
                result_list.append(index_set[i][1])
    return result_list

link = "https://forum.lowyat.net/"
l1_search = ["announce", "garage"] 

print(level1_scrape(link, l1_search))
