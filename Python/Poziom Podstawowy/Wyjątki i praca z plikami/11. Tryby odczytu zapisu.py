def format():
    plik = open("preData.txt", "r+") #PRE
    plik2 = open("data.txt", "a+") #ODP
    tab = []
    for x in plik:
        #plik2.write(x)
        tab.append(x)
    tab.reverse()
    for i in tab:
        plik2.write(i)
    plik.close()
    plik2.close()