def clearUnderscore(s):
    l = list( s )
    while "_" in l:
        l.remove("_")
    return l