def getData(x):
    plik = open( "data.txt", "r" )
    return plik.read(x)
    plik.close()