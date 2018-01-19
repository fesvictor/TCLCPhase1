from analysis_process.load_posts import load_posts


def test1():
    posts = load_posts('../_1_process_raw_data/output/sample_output.json')
    assert len(posts) == 2
    assert posts[0] == {
        'date': '2017-05-18 11:56:09',
        'value': "b'Report: Red Granite in talks with DOJ to settle 1MDB-linked lawsuit'",
        'source': 'facebook',
        'related_to': None,
        'semantic_value': None
    }
