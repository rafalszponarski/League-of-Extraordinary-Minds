def plot(data):
    for period, profit in data:
        print("#" * profit + str(profit) + ", " + period)
