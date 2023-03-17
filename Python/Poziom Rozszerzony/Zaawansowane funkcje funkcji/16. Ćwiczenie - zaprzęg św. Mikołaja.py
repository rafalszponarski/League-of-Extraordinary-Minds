def setHarness(minRP, **kwargs):
    reniferowie_moc = [(k, v) for k, v in kwargs.items()]
    reniferowie_moc.sort(key=lambda x: (-x[1], x[0]))
    suma_mocy = 0
    zaprzeg = []
    for r, moc in reniferowie_moc:
        if suma_mocy + moc >= minRP:
            zaprzeg.append(r)
        suma_mocy += moc
    return sorted(zaprzeg)
