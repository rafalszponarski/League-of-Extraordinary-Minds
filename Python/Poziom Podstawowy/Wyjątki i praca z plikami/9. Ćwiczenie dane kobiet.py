def modify():
    plik = open("women.txt", "w")
    plik2 = open("preWomen.txt", "r")
    wiersz = 0
    for i in plik2:
        wiersz += 1
        if int(i[9])%2 == 0:
            print(i)
            plik.write(i)
    plik.close()
    plik2.close()