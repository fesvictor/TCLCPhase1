from analysis_process._1_process_raw_data.parse_facebook import parse_facebook
def test1():
    parent_dir = '..'
    file_path = parent_dir + '/sample_data/facebook.csv'
    posts = parse_facebook(file_path)
    assert posts[0].value == "b'Report: Red Granite in talks with DOJ to settle 1MDB-linked lawsuit'"


