def maxPeriod(debt, equity ):
    x = 0
    while debt <= equity:
        debt *= 1.035
        x += 1
    return x