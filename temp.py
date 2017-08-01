# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

with open("data\scraperesults\lowyat\links_retrieved.txt", 'r') as f:
    for row in f:
        links_retrieved.append(row.strip())

links_retrieved = links_retrieved[1721::]
print(links_retrieved)