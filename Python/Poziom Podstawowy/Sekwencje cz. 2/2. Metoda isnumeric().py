def formatHeight( feet, inches ):
    if (feet.isnumeric() == True) and (inches.isnumeric() == True) and (int(inches) < 12):
        if inches[0] == "0" or feet[0] == "0":
            return 0
        else:    
            
            return f"{feet} ft {inches}"
    else:
        return 0