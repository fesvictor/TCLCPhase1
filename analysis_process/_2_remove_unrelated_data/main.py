from os import listdir
from analysis_process.log import log
from analysis_process._2_remove_unrelated_data.load_labels import load_labels
from analysis_process._2_remove_unrelated_data.label_post import label_post
from analysis_process.load_posts import load_posts
from analysis_process.save_posts import save_posts


def main():
    log("Loading english posts", 1)
    english_posts = load_posts('analysis_process/_1_process_raw_data/output/english.json')
    log("Loading english labels", 1)
    english_labels = get_english_labels()
    log("Labeling english posts", 1)
    label_post(english_posts, english_labels)
    log("Removing unrelated posts", 1)
    purified = [x for x in english_posts if len(x['related_to']) > 0]
    log("Number of removed posts = " + str(len(english_posts) - len(purified)), 1)
    log("Saving the purified english posts as english.json", 1)
    save_posts(purified, 'analysis_process/_2_remove_unrelated_data/english.json')

    log("Loading chinese posts", 1)
    chinese_posts = load_posts('analysis_process/_1_process_raw_data/output/chinese.json')
    log("Loading chinese labels", 1)
    chinese_labels = get_chinese_labels()
    log("Labeling chinese posts", 1)
    label_post(chinese_posts, chinese_labels)
    log("Removing unrelated posts", 1)
    purified = [x for x in chinese_posts if len(x['related_to']) > 0]
    log("Number of removed posts = " + str(len(chinese_posts) - len(purified)), 1)
    log("Saving the purified chinese posts as chinese.json", 1)
    save_posts(purified, 'analysis_process/_2_remove_unrelated_data/chinese.json')
    log("DONE.", 1)


def get_english_labels():
    labels_dir = 'data/target/'
    leaders = load_labels(labels_dir + 'leader.txt')
    parties = load_labels(labels_dir + 'party.txt')
    return leaders + parties

def get_chinese_labels():
    labels_dir = 'data/target/'
    leaders = load_labels(labels_dir + 'chinese_leader.txt')
    parties = load_labels(labels_dir + 'chinese_party.txt')
    return leaders + parties


def get_posts():
    posts_dir = 'analysis_process/_1_process_raw_data/output/all_output.json'
    return load_posts(posts_dir)
    # for file_name in listdir(posts_dir):
    #     result += load_posts(posts_dir + file_name)
    # return result


main()
