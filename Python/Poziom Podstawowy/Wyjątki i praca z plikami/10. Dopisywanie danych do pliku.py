def addData(x):
    plik = open( "data.txt", "a" )
    plik.write(str(x["PESEL"]) + ' ' + x["firstName"] + ' ' + x["familyName"] + '\n')
    plik.close()
    