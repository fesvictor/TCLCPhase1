import json

def save_posts(list_of_posts, file_name):
    with open(file_name, 'w+') as file:
        if hasattr(list_of_posts[0], '__dict__'):
            json.dump([ob.__dict__ for ob in list_of_posts], file, indent=2)
        else:
            json.dump([ob for ob in list_of_posts], file, indent=2)
