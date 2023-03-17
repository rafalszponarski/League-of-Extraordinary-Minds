def delNumber( t1, t2 ):
    for x in t2:
        while x in t1:
            t1.remove( x )
    return t1