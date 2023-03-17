def delKeys(d, *args):
    for i in args:
        d.pop(i, None)
        
    return d