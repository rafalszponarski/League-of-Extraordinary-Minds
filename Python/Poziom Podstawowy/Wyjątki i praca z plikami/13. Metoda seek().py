def replaceSign(x, y):
    plik = open("data.txt", "r+")
    plik.seek(x-1)
    plik.write(y)
    plik.close()
   