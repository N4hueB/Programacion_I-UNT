def validar_opcion(n_min, n_max)->int:
    opcion = input("ingrese una opcion: ")
    while True:
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion >= n_min and opcion <= n_max:
                return opcion
            else:
                opcion = input("ingrese una opcion: ")
        else:
                opcion = input("ingrese una opcion: ")

print(validar_opcion(1,10))