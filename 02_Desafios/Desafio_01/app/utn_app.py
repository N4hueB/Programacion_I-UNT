from validaciones import validar_opcion
from funciones import (
    mostrar_menu, play_sound, limpiar_pantalla
)

def utn_heroes_app():
    while True:
        mostrar_menu()
        opcion = validar_opcion(1,10)
        match opcion:
            case 1:
                print("opcion 1")
                play_sound()
            case 2:
                print("opcion 2")
                play_sound()
            case 3:
                print("opcion 3")
                play_sound()
            case 4:
                print("opcion 4")
                play_sound()
            case 5:
                print("opcion 5")
                play_sound()
            case 6:
                print("opcion 6")
                play_sound()
            case 7:
                print("opcion 7")
                play_sound()
            case 8:
                print("opcion 8")
                play_sound()
            case 9:
                print("opcion 9")
                play_sound()
            case 10:
                print("opcion 10")
                play_sound()
        limpiar_pantalla()

