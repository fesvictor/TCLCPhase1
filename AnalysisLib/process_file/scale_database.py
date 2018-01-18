def scale_database(FileName):
    scale_words = []
    
#    with open(FileName, "rb")as scale_file:
#        for line in scale_file:
#            scale_words.append(line.decode('utf-8').replace('\r\n','')) 
#            
    with open('TCLCPhase1' + FileName, "r", encoding = 'utf-8')as scale_file:
        for line in scale_file:
            scale_words.append(line.replace('\n','').replace('\ufeff',''))
    return scale_words