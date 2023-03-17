def grossPrice(netto, podatek=23):
    return round(netto+netto*podatek/100, 2)