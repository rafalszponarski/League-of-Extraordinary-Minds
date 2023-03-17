from fitness import bmi as b
def clientBmi( clientsData, clientId ):
    return b(*clientsData[clientId][4:])