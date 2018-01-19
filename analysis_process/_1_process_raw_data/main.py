from analysis_process._1_process_raw_data.store_output import store_output
from analysis_process._1_process_raw_data.parse_facebook import parse_facebook

parent_dir = 'analysis_process/_1_process_raw_data/'
result = parse_facebook(parent_dir + 'sample_data/facebook.csv')
store_output(result, 'facebook')
