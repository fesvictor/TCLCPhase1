#Query website URL
import urllib
import textwrap as tw
from bs4 import BeautifulSoup as bs
from ReadParameterFile import get_parameter_dict
import re #Regex library

def scrape(link, save_dir):
    link_suffix = "/all" #Used to read first 25 pages (limited to first 25 only)
    save_filename = link.strip("https://forum.lowyat.net/topic/")
    link = link + link_suffix
    
    #Query website
    page = urllib.request.urlopen(link)
    
    #Parse data returned from website
    soup = bs(page, "lxml")
    
    spoiler_text = "» Click to show Spoiler - click again to hide... «" #Appears when content hidden in spoilers
    
    #Used to pull raw HTML file
    #with open('raw_html.html', 'wb') as f:
    #   f.write(soup.prettify('utf8'))
        
    [div.extract() for div in soup.find_all("div", { "class" : "quotemain"})]   #Removes quote text
    [div.extract() for div in soup.find_all("div", { "class" : "quotetop"})]    #Removes quote timestamp
    fp = open(save_dir+'lowyat_'+save_filename+'.txt', 'a')
    fp.truncate(0)  #Clears the text file first
    for div in soup.find_all("div", { "class" : "postcolor post_text"}):    #Get all specific tags
        string = div.get_text()
        string = bytes(string, 'utf-8').decode('utf-8', 'ignore')
        string = string.replace(spoiler_text, ' ').strip()
        string = tw.fill(string, 120)
        fp.write(string)  #Get contents from the tags, text wrapping width 120
        fp.write('\n\r')    #New lines for text file
    fp.close()

def reassemble_link(topic_number):
    suffix = "https://forum.lowyat.net/topic/"
    reassembled = suffix + topic_number
    return reassembled
    
#main
parameter_dict = get_parameter_dict()
links_file = parameter_dict['scrap.links'].strip('./')  
save_dir = parameter_dict['lowyat.files'].strip('./')+'/'

#URL
with open(links_file, 'r') as fp:
    link_list = fp.readlines()
    link_list = [links for links in link_list if len(links) > 5] #Removes blank, typo rows in list
    link_list = [links.strip('\n') for links in link_list] #Removes newline characters from links
    link_list = [links.split('\t\t')[0] for links in link_list] #Ignore topic titles in link list
    
    #Check if links obtained are from forum search engine
    #Forum search engine returns links in a different format
    #Eg: https://forum.lowyat.net/index.php?showtopic=4318258&hl=barisan
    #Instead of https://forum.lowyat.net/topic/4318258
    for i in range(0, len(link_list)):

        if "index.php?showtopic=" in link_list[i]:
            regex = re.search('showtopic=(.+?)&hl', link_list[i])
            link_list[i] = regex.group(1)
            link_list[i] = reassemble_link(link_list[i])
    for links in link_list:
       scrape(links, save_dir)