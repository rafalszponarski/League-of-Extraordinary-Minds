def deviation(readings):
    mean = sum(readings) / len(readings)
    for reading in readings:
        deviation = reading - mean
        deviation_str = '{:.14f}'.format(deviation)
        if deviation >= 0:
            print(f"{'o'*(24-len(deviation_str))}{deviation_str}")
        else:
            print(f"{'-' + 'o'*(23-len(deviation_str))}{deviation_str}")
