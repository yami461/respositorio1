def validar_dato():
    while True:
        dato = input("Ingresa un valor entero (o escribe 'salir' para terminar): ")
        
        # Si el usuario escribe 'salir', termina el programa
        if dato.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        # Intentamos convertir el dato a un número entero
        try:
            numero_entero = int(dato)
            print("Has ingresado un número entero.")
        except ValueError:
            # Si no es posible convertirlo a entero, verifica si es un número decimal o texto
            try:
                numero_decimal = float(dato)
                print("Has ingresado un número decimal. Solo se permiten enteros.")
            except ValueError:
                print("Has ingresado un texto. Solo se permiten enteros.")

# Llamamos a la función
validar_dato()
