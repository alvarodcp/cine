# Inicializar las variables
opcion = -1
total_recaudado = 0
total_pagado = 0
capacidad = 0
precio_entrada = 0
precio_entrada_am = 0
precio_entrada_n = 0
tipo_entrada = -1 # los valores válidos son 0, entrada general, 1 niño, 2 adulto mayor

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
            cantidad_entradas = int(input("Digite la cantidad de entradas: "))
            if cantidad_entradas <= capacidad:
                capacidad = capacidad - cantidad_entradas
                total_pagado = cantidad_entradas * precio_entrada
                total_recaudado = total_recaudado + total_pagado
                print(f"El total a pagar por esta compra es {total_pagado}")
            else:
                print("La cantidad de entradas supera la capacidad disponible.")
        case 2:
            print(f"La capacidad actual de la sala es {capacidad}")
        case 3:
            print(f"El total recaudado es de: {total_recaudado}")
            print("Mostrar recaudación")
        case 4: # opción de configuración del sistema.
            capacidad = int(input("Digite la capacidad de la sala: "))
            precio_entrada = int(input("Digite el precio de la entrada general: "))
            precio_entrada_am = int(input("Digite el precio de la entrada para adultos mayores: "))
            precio_entrada_n = int(input("Digite el precio de la entrdada para niños: "))
        case 0:
            print("Cerrando el programa....")
            break
        case _:
            print("Valor inválido. Intente nuevamente")


