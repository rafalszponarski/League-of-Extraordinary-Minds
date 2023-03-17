def prize( days ):
    suma=0
    kwota=0
    for x in range(days):
        kwota += x + 1
        suma += kwota 
    return suma