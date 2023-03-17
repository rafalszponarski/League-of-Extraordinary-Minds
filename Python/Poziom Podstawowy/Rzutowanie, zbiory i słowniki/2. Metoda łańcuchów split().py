def selectAndSum( x ):
    x = x.split(", ")
    suma = 0
    for i in x:
        if i.isnumeric() == True:
            suma += int(i)
    return suma