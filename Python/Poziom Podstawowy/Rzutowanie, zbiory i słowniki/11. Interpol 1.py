def findSuspects(x, y, z):
    x = set(x)
    y = set(y)
    z = set(z)
    mozliwosc1 = x & y
    mozliwosc2 = x & z
    mozliwosc3 = y & z
    odp = mozliwosc1 | mozliwosc2 | mozliwosc3
    return odp