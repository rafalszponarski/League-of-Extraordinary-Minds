def convertList(values, bases):
    x = []
    for i in range(len(values)):
        try:
            int(str(values[i]), bases[i])
        except ValueError:
            x.append(values[i])
    
    return x    