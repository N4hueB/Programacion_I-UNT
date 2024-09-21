import pygame.mixer as mixer
import time

def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def play_sound():
    """
    The `play_sound` function initializes the mixer, loads a sound file, sets the volume to 0.4, and
    plays the sound.
    """
    mixer.init()
    mixer.music.load(r'C:\UTN\Programacion_I-UNT\Programacion_I-UNT\02_Desafios\Desafio_01\assets\snd\select.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()
    time.sleep(0.4)

def mostrar_nombre(lista_nombre, indice):
    """
    Documentacion
    """
    indice_actual = 0
    for nombre in lista_nombre:
        if indice_actual == indice:
            return nombre
        else:
            indice_actual += 1

def obtener_maximo(lista_numeros):
    numero_max = 0
    for numero in lista_numeros:
        if numero > numero_max:
            numero_max = numero
    numero_max = float(numero_max)
    return numero_max
