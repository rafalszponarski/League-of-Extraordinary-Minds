from datetime import datetime

def displayTime():
    time = datetime.now().strftime("%H:%M:%S")
    day = datetime.now().strftime("%A")
    return str(time) +' '+ str(day[0:3:].upper())