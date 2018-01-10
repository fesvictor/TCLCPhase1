from TCLCPhase1.get_parameter_dict import get_parameter_dict

def test():
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
