def testA( t1, t2 ):
    t10 = 0
    t20 = 0
    for i in t1:
        if i == "a":
            t10 += 1
    for i in t2:
        if i == "a":
            t20 += 1
    if t10 == t20:
        x= t1+t2
    elif t10 > t20:
        x= t1+t2
    else:
        x= t2+t1
    return x