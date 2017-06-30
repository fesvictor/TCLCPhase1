import scrapper.scraping as s
import re
from ReadParameterFile import get_parameter_dict

parameter_dict = get_parameter_dict()
links_file = parameter_dict['scrap.links'].strip('./')  
save_dir = parameter_dict['lowyat.files'].strip('./')+'/'

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
            link_list[i] = s.reassemble_link(link_list[i])
    for links in link_list:
       s.scrape(links, save_dir)

