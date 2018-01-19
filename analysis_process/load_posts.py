import json


def load_posts(file_path):
    with open(file_path) as file:
        posts = json.load(file)
        return posts