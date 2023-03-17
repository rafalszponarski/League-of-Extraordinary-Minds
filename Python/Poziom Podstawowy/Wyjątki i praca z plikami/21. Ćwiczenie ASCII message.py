def convertData(file):
    try:
        czytaj = open(file, "r")
    except IOError:
        return 1
    pisz = open("message.txt", "w")
    
    length = 0
    for line in czytaj:
        length += 1
    
    czytaj.seek(0)
    l = 0
    
    for line in czytaj:
        l += 1
        line = line.split()
        for data in line:
            try:
                data = int(data)
            except ValueError:
                return 2

            if data < 0 or data > 127:
                return 3

            pisz.write(chr(data))
        if l < length:
            pisz.write("\n")
    return 0