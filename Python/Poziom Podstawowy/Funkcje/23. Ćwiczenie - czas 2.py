def to_time(x):
    if x < 60:
        return x
    elif x == 60:
        return 100
    elif x > 60 and x < 3600:
        min = x//60
        s = x-60*(x//60)
        return (min*100)+s
    else:
        h = x//3600
        x = x-(3600*h)
        min = x // 60
        #x = x-60*min
        s = x - 60 * (x // 60)
        return (h * 10000) + (min*100) + s
