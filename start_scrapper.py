import scrapper.crawler as c
import scrapper.tlink_scraper as t
import scrapper.post_scrape as p

#To use scrapper, first setup the crawler
#Crawler returns of a list filtered by l1_search and l2_search list, to return ALL links, leave blank []
#Crawler currently limited to 2 levels of depth ie: /Kopitiam (Level1) & /Kopitiam/SeriousKopitiam

link = "https://forum.lowyat.net/"
levels = 1 #Max
l1_search = ["kopi"]
l2_search = ["serious"]

link_list = c.crawl_levels(link, levels, l1_search, l2_search)

#Next, setup thread links scraper
page_limit = 2
search_list = []
links_retrieved = []
for l in link_list:
    links_retrieved = links_retrieved + t.tlink_scrape(l, page_limit, search_list)
    print(links_retrieved)
    
#Finally, setup the post scraper
#Post scraper returns a dataframe, which can be output to a csv.
for l in links_retrieved:
    df = p.post_scrape(l)
    df.to_csv("posts.csv", mode='a', header=False)