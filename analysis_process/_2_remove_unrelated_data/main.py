from os import listdir
from analysis_process._2_remove_unrelated_data.load_labels import load_labels
from analysis_process._2_remove_unrelated_data.label_post import label_post
from analysis_process.load_posts import load_posts
from analysis_process.save_posts import save_posts


def main():
    print("Loading posts from all_output.json")
    all_posts = get_posts()
    print("Loadings labels")
    all_labels = get_labels()
    print("Labellig posts")
    label_post(all_posts, all_labels)
    print("Removing unrelated posts")
    purified = [x for x in all_posts if len(x['related_to']) > 0]
    print("Number of removed posts = " + str(len(all_posts) - len(purified)))
    print("Saving the purified posts into output.json")
    save_posts(purified, 'analysis_process/_2_remove_unrelated_data/output.json')
    print("DONE.")


def get_labels():
    labels_dir = 'data/target/'
    leaders = load_labels(labels_dir + 'leader.txt')
    parties = load_labels(labels_dir + 'party.txt')
    return leaders + parties


def get_posts():
    posts_dir = 'analysis_process/_1_process_raw_data/output/all_output.json'
    return load_posts(posts_dir)
    # for file_name in listdir(posts_dir):
    #     result += load_posts(posts_dir + file_name)
    # return result


main()
