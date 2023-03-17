def brutto( x ):
    x = x.split()
    x[0] = round(float(x[0])/100*8+float(x[0]), 2)
    return str(x[0])+" "+x[1]
