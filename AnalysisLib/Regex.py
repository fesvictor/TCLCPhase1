def search(toMatch, word):
    import re
    toMatch = toMatch.replace(".", "")
    toMatch = toMatch.replace("?", "")
    toMatch = toMatch.replace("*", "")
    toMatch = toMatch.lower()
    word = word.replace(" ",".*")
    p = re.compile(word)
    if p.search(toMatch):
        return True