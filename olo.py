def ReservarSalaConferencia():#alex
    pass

def ConsultarDisponibilidad():#akex
    pass

def AdministrarReservas():
    pass

def CargarReservas():
    pass

def GuardarReservas():
    pass

def menu():
    print("menu 1 2 3 4 5")
    op=int(input("pone tu caga"))
    if op==1:
        ReservarSalaConferencia()
    elif op==2:
        ConsultarDisponibilidad()
    elif op==3:
        AdministrarReservas()
    elif op==4:
        CargarReservas()
    elif op==5:
        GuardarReservas()
    
    pass
menu()
