def generateBilling(x):
    plik = open( "billing.txt", "w" )
    for el in x:
        plik.write(el[0] + ', ' + el[1] + ', ' + el[2] + '\n')
    plik.close()