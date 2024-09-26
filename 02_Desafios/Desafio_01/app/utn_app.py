from data_heroes import*
from validaciones import validar_opcion
from funciones import (
    mostrar_menu, play_sound, limpiar_pantalla, utn_mostrar_nombres_heroes, 
    utn_mostrar_identidades_heroes, utn_mostrar_heroe_mayor_altura,
    utn_mostrar_heroes_mas_fuertes, utn_filtrar_heroes_genero,utn_mostrar_heroes_poder_superior_promedio,
    utn_mostrar_heroes_mas_debiles, utn_mostrar_poder_ascendente, utn_mostrar_altura_descendente
)

def utn_heroes_app():
    while True:
        mostrar_menu()
        opcion = validar_opcion(1,13)
        match opcion:
            case 1:
                utn_mostrar_nombres_heroes(lista_nombres_heroes)
                play_sound()
            case 2:
                utn_mostrar_identidades_heroes(lista_identidades_heroes)
                play_sound()
            case 3:
                utn_mostrar_heroe_mayor_altura(lista_nombres_heroes,
                            lista_identidades_heroes,
                            lista_generos_heroes,
                            lista_alturas_heroes,
                            lista_poder_heroes)
                play_sound()
            case 4:
                utn_mostrar_heroes_mas_fuertes(lista_nombres_heroes,
                            lista_identidades_heroes,
                            lista_generos_heroes,
                            lista_alturas_heroes,
                            lista_poder_heroes)
                play_sound()
            case 5:
                utn_filtrar_heroes_genero(lista_nombres_heroes,
                            lista_identidades_heroes,
                            lista_generos_heroes,
                            lista_alturas_heroes,
                            lista_poder_heroes, "Femenino")
                play_sound()
            case 6:
                utn_filtrar_heroes_genero(lista_nombres_heroes,
                            lista_identidades_heroes,
                            lista_generos_heroes,
                            lista_alturas_heroes,
                            lista_poder_heroes, "Masculino")
                play_sound()
            case 7:
                utn_filtrar_heroes_genero(lista_nombres_heroes,
                            lista_identidades_heroes,
                            lista_generos_heroes,
                            lista_alturas_heroes,
                            lista_poder_heroes, "No-Binario")
                play_sound()
            case 8:
                utn_mostrar_heroes_poder_superior_promedio(lista_nombres_heroes,
                            lista_identidades_heroes,
                            lista_generos_heroes,
                            lista_alturas_heroes,
                            lista_poder_heroes)
                play_sound()
            case 9:
                utn_mostrar_heroes_mas_debiles(lista_nombres_heroes,
                            lista_identidades_heroes,
                            lista_generos_heroes,
                            lista_alturas_heroes,
                            lista_poder_heroes)
                play_sound()
            case 10:
                utn_mostrar_poder_ascendente(lista_nombres_heroes,
                            lista_identidades_heroes,
                            lista_generos_heroes,
                            lista_alturas_heroes,
                            lista_poder_heroes)
                play_sound()
            case 11:
                utn_mostrar_altura_descendente(lista_nombres_heroes,
                            lista_identidades_heroes,
                            lista_generos_heroes,
                            lista_alturas_heroes,
                            lista_poder_heroes)
                play_sound()
            case 12:
                pass
            case 13:
                play_sound()
                break
        limpiar_pantalla()

