from funciones import obtener_maximo
from funciones import promedio
from funciones import obtener_mitad_de_maximo

def utn_mostrar_nombres_heroes(lista_nombres):
    """
    Documentacion
    """
    for nombre in lista_nombres:
        print(nombre)

def utn_mostrar_identidades_heroes(lista_identidad):
    """
    Documentacion
    """
    for identidad in lista_identidad:
        print(identidad)

def utn_mostrar_heroe_mayor_altura(lista_nombre, lista_identidad, lista_genero, lista_altura, lista_poder):
    """
    Documentacion
    """
    print("{:<20} | {:<50} | {:^10} | {:>10} | {:>5}".format(
        "Nombre", "Identidad", "Género", "Altura", "Poder"))
    print("-" * 100)  # Línea divisoria para mejorar la legibilidad
    heroe_altura_max = obtener_maximo(lista_altura)
    indice = lista_altura.index(heroe_altura_max)
    print("{:<20} | {:<50} | {:^10} | {:>10.1f} | {:>5}".format(
                lista_nombre[indice],
                lista_identidad[indice],
                lista_genero[indice],
                lista_altura[indice],
                lista_poder[indice]))

def utn_mostrar_heroes_mas_fuertes(lista_nombre, lista_identidad, lista_genero, lista_altura, lista_poder):
    """
    Documentacion
    """
    heroe_poder_max = obtener_maximo(lista_poder)
    print("{:<20} | {:<50} | {:^10} | {:>10} | {:>5}".format(
        "Nombre", "Identidad", "Género", "Altura", "Poder"))
    print("-" * 100)  # Línea divisoria para mejorar la legibilidad

    indice = 0
    for heroe_max in lista_poder:
        if heroe_max == heroe_poder_max:
            print("{:<20} | {:<50} | {:^10} | {:>10.1f} | {:>5}".format(
                lista_nombre[indice],
                lista_identidad[indice],
                lista_genero[indice],
                lista_altura[indice],
                lista_poder[indice]))
        indice += 1


def utn_filtrar_heroes_genero(lista_nombre, lista_identidad, lista_genero, lista_altura, lista_poder, genero):
    """
    Documentacion
    """
    print("{:<20} | {:<50} | {:^10} | {:>10} | {:>5}".format(
        "Nombre", "Identidad", "Género", "Altura", "Poder"))
    print("-" * 100)  # Línea divisoria para mejorar la legibilidad

    for i in range(len(lista_genero)):
        if lista_genero[i] == genero:
            print("{:<20} | {:<50} | {:^10} | {:>10.1f} | {:>5}".format(
                lista_nombre[i],
                lista_identidad[i],
                lista_genero[i],
                lista_altura[i],
                lista_poder[i]))

def utn_mostrar_heroes_poder_superior_promedio(lista_nombre, lista_identidad, lista_genero, lista_altura, lista_poder):
    """
    Documentacion
    """
    print("{:<20} | {:<50} | {:^10} | {:>10} | {:>5}".format(
        "Nombre", "Identidad", "Género", "Altura", "Poder"))
    print("-" * 100)  # Línea divisoria para mejorar la legibilidad
    promedio_poder = promedio(lista_poder)
    for i in range(len(lista_poder)):
        if lista_poder[i] > promedio_poder:
            print("{:<20} | {:<50} | {:^10} | {:>10.1f} | {:>5}".format(
                lista_nombre[i],
                lista_identidad[i],
                lista_genero[i],
                lista_altura[i],
                lista_poder[i]))

def utn_mostrar_heroes_mas_debiles(lista_nombre, lista_identidad, lista_genero, lista_altura, lista_poder):
    """
    Documentacion
    """
    print("{:<20} | {:<50} | {:^10} | {:>10} | {:>5}".format(
        "Nombre", "Identidad", "Género", "Altura", "Poder"))
    print("-" * 100)  # Línea divisoria para mejorar la legibilidad
    poder_min = obtener_mitad_de_maximo(lista_poder)
    for i in range(len(lista_poder)):
        if lista_poder[i] < poder_min:
            print("{:<20} | {:<50} | {:^10} | {:>10.1f} | {:>5}".format(
                lista_nombre[i],
                lista_identidad[i],
                lista_genero[i],
                lista_altura[i],
                lista_poder[i]))

def utn_mostrar_poder_ascendente(lista_nombre, lista_identidad, lista_genero,
                            lista_altura, lista_poder):
    """
    Documentacion
    """
    print("{:<20} | {:<50} | {:^10} | {:>10} | {:>5}".format(
        "Nombre", "Identidad", "Género", "Altura", "Poder"))
    print("-" * 100)  # Línea divisoria para mejorar la legibilidad
    heroes = list(zip(lista_nombre, lista_identidad, lista_genero, lista_altura, lista_poder))    
    n = len(heroes)
    for i in range(n):
        for j in range(0, n-i-1):
            if heroes[j][-1] > heroes[j+1][-1]:
                heroes[j], heroes[j+1] = heroes[j+1], heroes[j]
    for i in range(len(heroes)):
        print("{:<20} | {:<50} | {:^10} | {:>10.1f} | {:>5}".format(
            heroes[i][0],
            heroes[i][1],
            heroes[i][2],
            heroes[i][3],
            heroes[i][4]
        ))

def utn_mostrar_altura_descendente(lista_nombre, lista_identidad, lista_genero,
                                lista_altura, lista_poder):
    """
    Documentación
    """
    print("{:<20} | {:<50} | {:^10} | {:>10} | {:>5}".format(
        "Nombre", "Identidad", "Género", "Altura", "Poder"))
    print("-" * 100)  # Línea divisoria para mejorar la legibilidad
    heroes = list(zip(lista_nombre, lista_identidad, lista_genero, lista_altura, lista_poder))

    # Ordenamiento por altura (descendente)
    for i in range(len(heroes) - 1):
        for j in range(i + 1, len(heroes)):
            if heroes[i][3] < heroes[j][3]:  # Comparar por el cuarto elemento (altura)
                heroes[i], heroes[j] = heroes[j], heroes[i]

    # Impresión de los resultados
    for hero in heroes:
        print("{:<20} | {:<50} | {:^10} | {:>10.1f} | {:>5}".format(
            hero[0], hero[1], hero[2], hero[3], hero[4]))