# Inicializar las variables
opcion = -1

# Mostrar el menú.
while True :
    print("1. Vender entrada.")
    print("2. Mostrar capacidad restante de la sala.")
    print("3. Mostrar total recaudado.")
    print("4. Configuración")
    print("0. Salir")
    # solicitar la opción al usuario
    opcion = int(input("Digite la opción: "))

    # se hace la evaluación de la opción
    match opcion:
        case 1:
            print("Vender entrada")
        case 2:
            print("Mostra capacidad")
        case 3:
            print("Mostrar recaudación")
        case 4:
            print("Configuración")
        case 0:
            print("Cerrando el programa....")
            break
        case _:
            print("Valor inválido. Intente nuevamente")
