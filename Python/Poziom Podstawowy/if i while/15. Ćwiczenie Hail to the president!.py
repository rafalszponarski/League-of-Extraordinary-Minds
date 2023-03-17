def play_anthem():
    note = get_note()
    while note != 0:
        play( note )
        note = get_note()