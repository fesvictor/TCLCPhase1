def scale_database(FileName):
    scale_words = []
    with open(FileName, "rb")as scale_file:
        for line in scale_file:
            scale_words.append(line.decode('utf-8').replace('\r\n',''))   
    return scale_words