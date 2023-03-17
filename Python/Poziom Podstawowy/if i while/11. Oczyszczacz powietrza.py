def setPower( pm25, pm10 ):
    if pm25 > 120 or pm10 > 200:
        return 5
    elif pm25 >= 85 or pm10 >=141:
        return 4
    elif pm25 >= 61 or pm10 >=101:
        return 3
    elif pm25 >= 37 or pm10 >=61:
        return 2
    elif pm25 >= 13 or pm10 >=21:
        return 1
    else:
        return 0    