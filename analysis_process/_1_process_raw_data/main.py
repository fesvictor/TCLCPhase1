import os
from analysis_process.save_posts import save_posts
from analysis_process._1_process_raw_data.parse_facebook import parse_facebook
from analysis_process._1_process_raw_data.parse_blog import parse_blog

PARENT_DIR = 'data/scraperesults/'
FACEBOOK_DIR = PARENT_DIR + 'facebook/'
BLOG_DIR = PARENT_DIR + 'blog/'


def main():
    parse_files_from(FACEBOOK_DIR, parse_facebook)
    parse_files_from(BLOG_DIR, parse_blog)


def parse_files_from(directory, parser):
    posts = []
    for file in os.listdir(directory):
        posts += parser(directory + file)
        save_posts(posts, f'analysis_process/_1_process_raw_data/output/{file.replace(".csv", "")}.json')


main()
