from os import listdir
from analysis_process._2_remove_unrelated_data.load_labels import load_labels
from analysis_process.load_posts import load_posts
from analysis_process.save_posts import save_posts


def main():
    all_posts = get_posts()
    all_labels = get_labels()
    for post in all_posts:
        for label in all_labels:
            if label in post['value']:
                post['related_to'] = label
    purified = [x for x in all_posts if x['related_to'] is not None]
    save_posts(purified, 'analysis_process/_2_remove_unrelated_data/output.json')


def get_labels():
    labels_dir = 'data/target/'
    leaders = load_labels(labels_dir + 'leader.txt')
    parties = load_labels(labels_dir + 'party.txt')
    return leaders + parties


def get_posts():
    posts_dir = 'analysis_process/_1_process_raw_data/output'
    result = []
    for file_name in listdir(posts_dir):
        result += load_posts(posts_dir + '/' + file_name)
    return result


main()
