import math
def format():
    plik = open("preData.txt", "r+") #PRE
    plik2 = open("data.txt", "w+") #ODP
    tab = []
    licznik = 0
    for i in plik:
        tab.append(i)

    for i in tab:
        tab[licznik] = tab[licznik][0:2]
        licznik += 1

    for i in tab:
        plik2.write(i + ' ' + str(math.sqrt(int(i))) + '\n')

    plik.close()
    plik2.close()
