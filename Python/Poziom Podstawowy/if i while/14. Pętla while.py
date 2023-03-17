def printer_ctrl():
    while pc_leftover() > 5:
        pc_cut()
        pc_position()
        pc_print()
    pc_pause()