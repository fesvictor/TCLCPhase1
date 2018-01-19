import json

def save_posts(list_of_posts, file_name):
    with open(file_name, 'w+') as file:
        json.dump([ob.__dict__ for ob in list_of_posts], file, indent=2)
    
