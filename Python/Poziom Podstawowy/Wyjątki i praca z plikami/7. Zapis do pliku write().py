plik = open( "prime_numbers.txt", "w" )
tab  = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47']
for i in tab:
    plik.write(i+"\n")
plik.close()