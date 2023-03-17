def outgoings(x):
    suma = 0
    for y in x:
        try:
            if y < 0:
                suma += y
        except:
            pass
    
    return suma