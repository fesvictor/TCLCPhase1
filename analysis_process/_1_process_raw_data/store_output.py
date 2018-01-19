import json

def store_output(list_of_posts, source):
    parent_dir = 'analysis_process/_1_process_raw_data/'
    file_dir = parent_dir + 'output/' + source + '_output.json'
    with open(file_dir, 'w+') as file:
        json.dump([ob.__dict__ for ob in list_of_posts], file, indent=2)
    
