import re
axe = "BN party is for development"
axe = axe.replace(" "," *")
print(axe)
p =re.compile(axe)
if p.search("fuck BN party is   for       developmentqqqq nonoo", re.IGNORECASE):
    print("hi")

#if re.search('bas is not bus', 'bas is not bus', re.IGNORECASE):
#    print("hi")

#if re.search('axe', 'Axe aXe aXE', re.IGNORECASE):
#    print("1")

#p =re.compile("bca*t")
#print(p.search(""))

class MatchWord:
    def __init__(self):
        self.match_cnt = 0
        self.word_list = None

    def printHi(self):
        print(self.match_cnt)
        print(self.word_list)
    
    def record(self, _wordlist, _cnt):
        self.word_list = _wordlist
        self.match_cnt = _cnt

MatchWord_list = []

ss = ["0","worst     party   ever   in the history", "hi bello history", "worst party ever"]
_sentence = "worst and rotten party everin the history"

for s in ss:
    _cnt = 0
    x = MatchWord()    
    _list = s.split()    
    
    for _word in _list:
        if _word in _sentence:
            _cnt += 1
            
    x.record(_list, _cnt)   
    if MatchWord_list == []:   
        MatchWord_list.append(x)
    else:
        for index, Obj in enumerate(MatchWord_list,0):
            if _cnt >= Obj.match_cnt:
                MatchWord_list.insert(index, x)
                break
            
            elif Obj == MatchWord_list[-1]:
                MatchWord_list += [x]
                break

for Obj in MatchWord_list:
    Obj.printHi()