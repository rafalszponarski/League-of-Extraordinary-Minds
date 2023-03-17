def getData( fileName ):
    plik = open( fileName, "r" )
    tablica = plik.readlines()
    string1 = ''
    for i in tablica:
        string1 += i[0]
    return string1
    plik.close()