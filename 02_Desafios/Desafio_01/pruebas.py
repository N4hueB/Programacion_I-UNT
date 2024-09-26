# lista_desordenada = [5, 2, 1, 55, 84, 13, 20, 11, 10]
# lista = [5, 2, 1, 55, 84, 13, 20, 11, 10]

#################### BUBBLE SORT ####################
# flag = False
# while flag == False:
#     flag = True
#     for i in range(len(lista)-1):
#         if lista[i] > lista[i + 1]:
#             aux = lista[i]
#             lista[i] = lista[i + 1]
#             lista[i + 1] = aux
#             flag = False

# print(lista_desordenada)
# print(lista)

#################### SELECTION SORT ####################
# tamaño_lista = len(lista)
# for i in range(0, tamaño_lista):
#     min = i
#     for j in range(i + 1, tamaño_lista):
#         if lista[min] > lista[j]:
#             min = j
#     aux = lista[i]
#     lista[i] = lista[min]
#     lista[min] = aux

# print(lista_desordenada)
# print(lista)

#################### QUICK SORT ####################
# def particionado(lista):
#     tamaño_lista = len(lista)
#     pivote = lista[0]
#     menores = []
#     mayores = []
#     for i in range(1, tamaño_lista):
#         if lista[i] < pivote:
#             menores.append(lista[i])
#         else:
#             mayores.append(lista[i])
#     return menores, pivote, mayores

# def quicksort(lista):
#     if len(lista) < 2:
#         return lista
#     menores, pivote, mayores = particionado(lista)
#     return quicksort(menores) + [pivote] + quicksort(mayores)

# print(quicksort(lista))


lista_nombres_heroes = [
    "Jason Bourne",
    "T-800",
    "Bumblebee",
    "Ben 10",
    "Power Girl",
    "Predator",
    "Rambo",
    "Sauron",
    "Batman",
    "White Canary",
    "Thanos",
    "Goblin Queen",
    "Captain Marvel",
    "Black Adam",
    "One Punch Man",
    "Snowbird",
    "Killer Frost",
    "Indiana Jones",
    "Hit-Girl",
    "Kick-Ass",
    "Godzilla",
    "Iron Man",
    "John Constantine",
    "Faora",
    "Chuck Norris",
    "Black Canary",
    "Spock",
    "Vegeta",
    "Venom",
    "Wonder Girl",
    "Captain America",
    "Darkseid",
    "Goku",
    "Han Solo",
    "Hancock",
    "Harry Potter",
    "Naruto Uzumaki"
]

lista_identidades_heroes = [
    "Delta Uno",
    "Cyberdyne Systems Series 800 Terminator Model 101",
    "Karen Beecher",
    "Benjamin Kirby Tennyson",
    "Kara Zor-L",
    "Yautja",
    "John Rambo",
    "Sauron",
    "Bruce Wayne",
    "Sara Lance",
    "Thanos",
    "Madelyne Jennifer Pryor",
    "Billy Batson",
    "Teth-Adam",
    "Saitama",
    "Narya",
    "Caitlin Snow",
    "Indiana Jones",
    "Mindy McCready",
    "Dave Lizewski",
    "Gojira",
    "Tony Stark",
    "John Constantine",
    "Faora Hu-Ul",
    "Carlos Ray Norris",
    "Dinah Drake Lance",
    "S'chn T'gai Spock",
    "Vegeta",
    "Eddie Brock",
    "Cassandra Elizabeth Sandsmark",
    "Steve Rogers",
    "Uxas",
    "Kakarot",
    "Han Solo",
    "John Hancock",
    "Harry James Potter",
    "Naruto Uzumaki"
]

lista_generos_heroes = [
    "Masculino",
    "Masculino",
    "Femenino",
    "Masculino",
    "Femenino",
    "Masculino",
    "Masculino",
    "Masculino",
    "Masculino",
    "Femenino",
    "Masculino",
    "Femenino",
    "Masculino",
    "Masculino",
    "Masculino",
    "Femenino",
    "Femenino",
    "Masculino",
    "Femenino",
    "Masculino",
    "No-Binario",
    "Masculino",
    "Masculino",
    "Femenino",
    "Masculino",
    "Femenino",
    "Masculino",
    "Masculino",
    "Masculino",
    "Femenino",
    "Masculino",
    "Masculino",
    "Masculino",
    "Masculino",
    "Masculino",
    "Masculino",
    "Masculino"
]

lista_alturas_heroes = [
    168,
    188,
    170.0,
    161.54,
    180.0,
    213.0,
    178.0,
    279.0,
    188.0,
    165,
    201.0,
    168.0,
    193.0,
    191.0,
    175.0,
    178.0,
    162,
    183.0,
    163,
    180,
    119000,
    198.0,
    183.0,
    177,
    178.0,
    165.0,
    185.0,
    168.0,
    191.0,
    165.0,
    188.0,
    267.0,
    175.0,
    183.0,
    188.0,
    168,
    168.0
]

lista_poder_heroes = [
    26,
    73,
    47,
    90,
    100,
    100,
    30,
    100,
    47,
    49,
    100,
    65,
    100,
    100,
    55,
    70,
    59,
    19,
    27,
    22,
    100,
    100,
    54,
    98,
    42,
    45,
    56,
    100,
    86,
    39,
    60,
    100,
    100,
    43,
    100,
    100,
    100
]



# # def mostrar_altura_descendente(lista):
# #     tamaño_lista = len(lista)
# #     for i in range(0, tamaño_lista):
# #         min = i
# #         for j in range(i + 1, tamaño_lista):
# #             if lista[min] < lista[j]:
# #                 min = j
# #         aux = lista[i]
# #         lista[i] = lista[min]
# #         lista[min] = aux
# #     return lista


# lista_nombres_heroes = [
#     "Jason Bourne",
#     "T-800",
#     "Bumblebee",
#     "Ben 10",
#     "Power Girl"]

# lista_identidades_heroes = [
#     "Delta Uno",
#     "Cyberdyne Systems Series 800 Terminator Model 101",
#     "Karen Beecher",
#     "Benjamin Kirby Tennyson",
#     "Kara Zor-L"]

# lista_generos_heroes = [
#     "Masculino",
#     "Masculino",
#     "Femenino",
#     "Masculino",
#     "Femenino"]

# lista_alturas_heroes = [
#     168,
#     188,
#     170.0,
#     161.54,
#     180.0]

# lista_poder_heroes = [
#     26,
#     73,
#     47,
#     90,
#     100]


#################### QUICK SORT ####################
def particionado(lista):
    tamaño_lista = len(lista)
    pivote = lista[0]
    menores = []
    mayores = []
    for i in range(1, tamaño_lista):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores, pivote, mayores

def quicksort(lista):
    if len(lista) < 2:
        return lista
    menores, pivote, mayores = particionado(lista)
    return quicksort(menores) + [pivote] + quicksort(mayores)

def utn_mostrar_poder_asc_des(lista_nombre, lista_identidad, lista_genero,
                            lista_altura, lista_poder):
    """
    Documentacion
    """
    print("{:<20} | {:<50} | {:^10} | {:>10} | {:>5}".format(
        "Nombre", "Identidad", "Género", "Altura", "Poder"))
    print("-" * 100)  # Línea divisoria para mejorar la legibilidad
    heroes = list(zip(lista_nombre, lista_identidad, lista_genero, lista_altura, lista_poder))  

    for i in range(len(heroes)):
        print("{:<20} | {:<50} | {:^10} | {:>10.1f} | {:>5}".format(
            heroes[i][0],
            heroes[i][1],
            heroes[i][2],
            heroes[i][3],
            heroes[i][4]
        ))


utn_mostrar_poder_asc_des(lista_nombres_heroes, lista_identidades_heroes, lista_generos_heroes,
                        lista_alturas_heroes, lista_poder_heroes)

