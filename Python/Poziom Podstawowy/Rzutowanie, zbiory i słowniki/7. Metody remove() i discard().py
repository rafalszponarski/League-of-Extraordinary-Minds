def clearData( x, y ):
    new = x.copy()
    for i in x:
        if int(i[1]) > int(y):
            new.discard(i)
    return new
    
    
    