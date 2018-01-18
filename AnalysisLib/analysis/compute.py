def compute(word):
    #print(word)
    global i
    global yearTable
    word[0] = word[0].lower()
    mutex.acquire()
    for party in party_list: #search if any party name in the sentence
        if party.getName() in word[0]: # if sentence contains words found in scale database
            #attitude likert scale
            if search_scale("Attitude",1,word[0]): # search whether this word in database
                i += 1
                add_scale(word[3], word[2], word[1], party.getName(), 0, "party")
            elif search_scale("Attitude",2,word[0]):
                i += 1
                add_scale(word[3], word[2], word[1], party.getName(), 1, "party")
       
    #for govtPolicy in govtPolicy_list: 
    #    if govtPolicy.getName() in word[0]: 
    #        #perception likert scale
    #        if search_scale("Perception",1,word[0]): 
    #            yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 0, "policy")
    #        elif search_scale("Perception",2,word[0]):
    #            yearTable = Year.addScale(yearTable, word[3], word[2], word[1], govtPolicy.getName(), 1, "policy")
    
    for leader in leader_list: 
        if leader.getName() in word[0]: 
            #popularity likert scale
            if search_scale("Popularity", 1, word[0]):
                i += 1
                add_scale(word[3], word[2], word[1], leader.getName(), 0, "leader")
            elif search_scale("Popularity", 2, word[0]):
                i += 1
                add_scale(word[3], word[2], word[1], leader.getName(), 1, "leader")
    mutex.release()