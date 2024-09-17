def validar_opcion(n_min, n_max)-> int:
    '''
    Documentacion
    '''
    opcion = input("Ingresa una opcion: ")
    while True:
        if opcion.isdigit():
            opcion = int(opcion)
            if n_min <= opcion <= n_max:
                return opcion
            else:
                print("Opcion fuera de rango")
                opcion = input("Ingresa una opcion: ")
        else:
            print("Debe ingresar un numero dentro del rango")
            opcion = input("Ingresa una opcion: ")
