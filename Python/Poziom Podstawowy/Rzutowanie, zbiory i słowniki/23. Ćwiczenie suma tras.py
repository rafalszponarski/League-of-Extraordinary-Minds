import delivery
def totalRoute():
    suma = 0
    for i in delivery.robots():
        suma += delivery.get(i)['data']['distanceToday']
    return suma