from analysis_process._1_process_raw_data.parse_facebook import parse_facebook
from analysis_process.save_posts import save_posts

parent_dir = 'analysis_process/_1_process_raw_data/'
result = parse_facebook(parent_dir + 'sample_data/facebook.csv')
save_posts(result, parent_dir +  'output/facebook_output.json')
