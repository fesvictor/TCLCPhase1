#Query website URL
import urllib
import textwrap as tw
from bs4 import BeautifulSoup as bs

#URL
lyn = 'https://forum.lowyat.net/topic/4306175'

#Query website
page = urllib.request.urlopen(lyn)

#Parse data returned from website
soup = bs(page, 'html.parser')

[div.extract() for div in soup.find_all("div", { "class" : "quotemain"})]   #Removes quote text
[div.extract() for div in soup.find_all("div", { "class" : "quotetop"})]    #Removes quote timestamp

fp = open('results\extracted.txt', 'a')
fp.truncate(0)  #Clears the text file first
for div in soup.find_all("div", { "class" : "postcolor post_text"}):    #Get all specific tags
    fp.write(tw.fill(div.get_text().strip(), 120))  #Get contents from the tags, text wrapping width 120
    fp.write('\n\r')    #New lines for text file
fp.close()