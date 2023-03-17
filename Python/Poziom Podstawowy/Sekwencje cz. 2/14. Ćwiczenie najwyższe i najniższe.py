def highLow( t1, t2 ):
    x = t1 + t2
    x.sort(reverse = True)
    y=[x[0], x[1], x[2], x[-3], x[-2], x[-1]]
    return y
    
    
