def findData( x ):
    plik = open("data.txt", "r")
    for i in plik:
        if int(i[0:11]) == x:
            return i[12:-1]
    plik.close()