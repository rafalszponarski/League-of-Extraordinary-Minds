def avgParticles( file ):
    try:
        plik = open(file, "r+")
    except FileNotFoundError:
        return "file not found"
    suma = 0
    ilosc = 0
    for i in plik:
        try:
            suma += int(i)
            ilosc += 1
        except:
            return "wrong data"
    
    return suma/ilosc    
