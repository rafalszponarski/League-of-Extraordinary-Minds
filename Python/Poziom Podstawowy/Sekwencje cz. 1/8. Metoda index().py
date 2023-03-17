def formatName( name ):
    x=int(name.index("_"))
    return name[0:x] +name[x+1].upper() +  name[x+2:]