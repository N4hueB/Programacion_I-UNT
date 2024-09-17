"""
Documentacion
"""
def validar_opcion(n_min, n_max)->int:
    '''
    Documentacion de la funcion
    '''
    opcion = input("ingrese una opcion: ")
    while True:
        if opcion.isdigit():
            opcion = int(opcion)
            if n_min <= opcion <= n_max:
                return opcion
            else:
                opcion = input("ingrese una opcion: ")
        else:
            opcion = input("ingrese una opcion: ")
