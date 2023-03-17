def get_initials( name ):
    x=int(name.index(" "))
    return name[0].upper() + name[x+1].upper()