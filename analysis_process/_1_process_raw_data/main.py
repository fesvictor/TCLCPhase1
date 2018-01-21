import os
from analysis_process.save_posts import save_posts
from analysis_process._1_process_raw_data.parse_blog import parse_blog
from analysis_process._1_process_raw_data.parse_facebook import parse_facebook
from analysis_process._1_process_raw_data.parse_lowyat import parse_lowyat
from analysis_process._1_process_raw_data.parse_twitter import parse_twitter

PARENT_DIR = 'data/scraperesults/'
FACEBOOK_DIR = PARENT_DIR + 'facebook/'
BLOG_DIR = PARENT_DIR + 'blog/'
LOWYAT_DIR = PARENT_DIR + 'lowyat/'
TWITTER_DIR = PARENT_DIR + 'twitter/'


def main():
    all_posts = []
    all_posts += parse_files_from(FACEBOOK_DIR, parse_facebook, "Parsing files from facebook")
    all_posts += parse_files_from(BLOG_DIR, parse_blog, "Parsing files from blog")
    all_posts += parse_files_from(LOWYAT_DIR, parse_lowyat, "Parsing files from lowyat")
    all_posts += parse_files_from(TWITTER_DIR, parse_twitter, "Parsing files from twitter")
    print("Saving Posts as all_output.json")
    save_posts(all_posts, f'analysis_process/_1_process_raw_data/output/all_output.json')
    print("Number of posts created : " + str(len(all_posts)))
    print("DONE.")

def parse_files_from(directory, parser, whats_happening):
    print(whats_happening)
    posts = []
    for file in os.listdir(directory):
        if not file.endswith('.csv'): 
            continue
        posts += parser(directory + file)
    return posts


main()
