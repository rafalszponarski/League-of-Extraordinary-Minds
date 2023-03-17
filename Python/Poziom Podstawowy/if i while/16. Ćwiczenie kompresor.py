def compressor( set_pressure ):
    while get_pressure() < set_pressure:
        pump()