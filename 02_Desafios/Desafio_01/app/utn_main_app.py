'''
Documentacion
'''
from funciones.salida_consola import mostrar_menu
from validaciones.validaciones import validar_opcion

def utn_heroes_app():
    '''
    Documentacion
    '''
    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 10)
        match opcion:
            case 1:
                print("opcion 1")
            case 2:
                print("opcion 2")
            case 3:
                print("opcion 3")
            case 4:
                print("opcion 4")
            case 5:
                print("opcion 5")
            case 6:
                print("opcion 6")
            case 7:
                print("opcion 7")
            case 8:
                print("opcion 8")
            case 9:
                print("opcion 9")
            case 10:
                print("opcion 10")

