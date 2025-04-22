import pygetwindow as gw



def detectar_ventanas(condicion):
    ventanas = gw.getWindowsWithTitle(condicion)
    # print(ventanas[0])
    return ventanas[0]

