def toUpper(t, *args):
    s = ''
    for i in t:
        if i.upper() in list(args) or i.lower() in list(args):
            s += i.upper()
        else:
            s += i
    return s
    