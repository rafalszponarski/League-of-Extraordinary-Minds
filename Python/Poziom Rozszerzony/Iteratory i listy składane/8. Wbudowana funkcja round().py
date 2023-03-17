def avgTempPerHour(temperatures):
    return [round(sum(part)/4, 1) for part in temperatures]
