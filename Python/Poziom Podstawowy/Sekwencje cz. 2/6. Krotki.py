def findLongest( x ):
    naj=0
    for i in x:
        if len(i)>naj:
            naj = len(i)
    return naj