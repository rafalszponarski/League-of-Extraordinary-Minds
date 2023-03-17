def findLongest(x):
    naj=0
    odp = 0
    for i in x:
        if len(i) != naj:
            if len(i) > naj:
                naj = len(i)
                odp = x.index(i)
    return x[odp]