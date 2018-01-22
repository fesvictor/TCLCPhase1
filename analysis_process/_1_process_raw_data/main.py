import os
from analysis_process.log import log
from analysis_process.save_posts import save_posts
from analysis_process._1_process_raw_data.parse_blog import parse_blog
from analysis_process._1_process_raw_data.parse_facebook import parse_facebook
from analysis_process._1_process_raw_data.parse_jbtalks import parse_jbtalks
from analysis_process._1_process_raw_data.parse_lowyat import parse_lowyat
from analysis_process._1_process_raw_data.parse_twitter import parse_twitter

PARENT_DIR = 'data/scraperesults/'
FACEBOOK_DIR = PARENT_DIR + 'facebook/'
BLOG_DIR = PARENT_DIR + 'blog/'
LOWYAT_DIR = PARENT_DIR + 'lowyat/'
TWITTER_DIR = PARENT_DIR + 'twitter/'
JBTALKS_DIR = PARENT_DIR + 'chinese/jbtalks/'


def main():
    english_posts = []
    log("Parsing english posts", 1)
    english_posts += parse_files_from(BLOG_DIR, parse_blog, "Parsing files from blog")
    english_posts += parse_files_from(FACEBOOK_DIR, parse_facebook, "Parsing files from facebook")
    english_posts += parse_files_from(LOWYAT_DIR, parse_lowyat, "Parsing files from lowyat")
    english_posts += parse_files_from(TWITTER_DIR, parse_twitter, "Parsing files from twitter")
    log("Saving english posts as english.json", 1)
    save_posts(english_posts, f'analysis_process/_1_process_raw_data/output/english.json')
    log("Number of english posts created : " + str(len(english_posts)), 1)
    log("Parsing chinese posts", 1)
    chinese_posts = []
    chinese_posts += parse_files_from(JBTALKS_DIR, parse_jbtalks, "Parsing files from jbtalks")
    log("Saving chinese posts as chinese.json", 1)
    save_posts(chinese_posts, f'analysis_process/_1_process_raw_data/output/chinese.json')
    log("DONE.", 1)


def parse_files_from(directory, parser, whats_happening):
    log(whats_happening, 2)
    posts = []
    for file in os.listdir(directory):
        if not file.endswith('.csv'):
            continue
        posts += parser(directory + file)
    return posts


main()
