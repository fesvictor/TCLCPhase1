# The 2 lines below allow you to import modules from parent directory
# For more info, refer https://stackoverflow.com/questions/16780014/import-file-from-parent-directory/16780068
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test():
    from get_parameter_dict import get_parameter_dict
    expected = {
        'facebook.files':            './data/scraperesults/facebook',
        'json.files':                './data/scraperesults/json',
        'lowyat.files':              './data/scraperesults/lowyat',
        'malaysiakini.files':        './data/scraperesults/malaysiakini',
        'output.dir':                './results',
        'polarity.political':        './data/categories/polarity',
        'policies.perception.scale': './data/categories/perceptions',
        'political.attitudes.scale': './data/categories/attitudes',
        'popular.political':         './data/categories/popularity',
        'regex.files':               './AnalysisLib',
        'scrap.links':               'scrap_links.txt',
        'target':                    './data/target',
        'temp.facebook.dir':         './temp/facebook',
        'temp.others.dir':           './temp/others',
        'temp.tweet.dir':            './temp/twitter',
        'twitter.files':             './data/scraperesults/twitter'
    }
    assert get_parameter_dict() == expected
