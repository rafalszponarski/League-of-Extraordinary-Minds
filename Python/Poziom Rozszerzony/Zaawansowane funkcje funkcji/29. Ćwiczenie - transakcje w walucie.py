def calcExchangeList(exRates, transactions, currency):
    #x = []
    #for i in transactions:
    #    if i[1] == currency:
    #        x.append(round(i[0]*exRates[currency], 2))
    
    #return x
    #return [round(i[0]*exRates[currency], 2) for i in transactions if i[1] == currency]      
    #return list(map(lambda i: round(i[0]*exRates[currency], 2), transactions))
    return list(map(lambda x: x[0] ,filter(lambda x: x[1] == currency, map(lambda i: (round(i[0]*exRates[currency], 2), i[1]), transactions))))
