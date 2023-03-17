def USToISO8601( dateList ):
    return [x[6:] + '-' + x[:2] + '-' + x[3:5] for x in dateList]