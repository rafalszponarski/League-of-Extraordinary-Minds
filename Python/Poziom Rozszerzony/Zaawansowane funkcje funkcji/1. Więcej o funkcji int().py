def convertList( values, bases ):
    #x = []
    #for i in range(len(values)):
    #    x.append(int(str(values[i]), bases[i]))
    #return x
    
    return [int(str(values[i]), bases[i]) for i in range(len(values))]