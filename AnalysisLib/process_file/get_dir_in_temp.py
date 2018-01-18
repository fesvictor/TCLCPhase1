def get_dir_in_temp(_dir): #(replcaed)
    from os import makedirs
    from os.path import exists
    from time import strftime
    if not exists(_dir + "/" + strftime("%Y") + "/" + strftime("%B")):
        makedirs(_dir + "/" + strftime("%Y") + "/" + strftime("%B"))
    return _dir + "/" + strftime("%Y") + "/" + strftime("%B")