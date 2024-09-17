# import pygame.mixer as mixer
# import time

# def validar_opcion(n_min, n_max)-> int:
#     '''
#     Documentacion
#     '''
#     opcion = input("Ingresa una opcion: ")
#     while True:
#         if opcion.isdigit():
#             opcion = int(opcion)
#             if n_min <= opcion <= n_max:
#                 return opcion
#             else:
#                 print("Opcion fuera de rango")
#                 opcion = input("Ingresa una opcion: ")
#         else:
#             print("Debe ingresar un numero dentro del rango")
#             opcion = input("Ingresa una opcion: ")

# def mostrar_menu()->str:
#     menu =  """
#     1  - Mostrar los nombres de los heroes
#     2  - Mostrar la identidad de los heroes
#     3  - Mostrar al heroe con mayor altura
#     4  - Mostrar al/los heroe/s con mayor poder, en caso de haber mas de uno, mostrarlos a todos.
#     5  - Filtrar a los heroes Femeninos y mostrar sus nombres
#     6  - Filtrar a los heroes Masculinos y mostrar sus identidades
#     7  - Filtrar a los personajes No-Binarios y mostrar su nombre e identidad
#     8  - Determinar cuales heroes tienen un poder superior al promedio.
#     9  - Determinar cual es el maximo de poder y mostrar los nombres de cuales heroes tienen un poder 
#         inferior A LA MITAD DE PODER del heroe mas fuerte.
#     10 - Salir
#             """
#     print(menu)

# def limpiar_pantalla():
#     """
#     The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
#     """
#     import os
#     _ = input("\nPresiona Enter para continuar...")
#     os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

# def play_sound():
#     """
#     The `play_sound` function initializes the mixer, loads a sound file, sets the volume to 0.4, and
#     plays the sound.
#     """
#     mixer.init()
#     mixer.music.load(r'C:\UTN\Programacion_I-UNT\Programacion_I-UNT\02_Desafios\Desafio_01\assets\snd\select.mp3')
#     mixer.music.set_volume(0.4)
#     mixer.music.play()
#     time.sleep(0.4)


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

utn_heroes_app()
