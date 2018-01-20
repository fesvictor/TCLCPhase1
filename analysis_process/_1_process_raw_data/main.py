import os
from analysis_process.save_posts import save_posts
from analysis_process._1_process_raw_data.parse_facebook import parse_facebook
from analysis_process._1_process_raw_data.parse_blog import parse_blog

PARENT_DIR = 'data/scraperesults/'
FACEBOOK_DIR = PARENT_DIR + 'facebook/'
BLOG_DIR = PARENT_DIR + 'blog/'
ALL_POSTS = []


for file in os.listdir(FACEBOOK_DIR):
    ALL_POSTS += parse_facebook(FACEBOOK_DIR + file)

for file in os.listdir(BLOG_DIR):
    ALL_POSTS += parse_blog(BLOG_DIR + file)

save_posts(ALL_POSTS, 'analysis_process/_1_process_raw_data/output/all_output.json')


