  # Importa el módulo re para trabajar con expresiones regulares (detección de símbolos)
import re

# Inicia un bucle infinito hasta que el usuario ingrese un número entero válido
while True:
    # Solicita al usuario que escriba algo
    entrada_usuario = input("Ingresa un número entero: ")

    # Intenta convertir la entrada directamente a entero
    try:
        numero_ingresado = int(entrada_usuario)
        break  # Si la conversión es exitosa, salimos del bucle
    except ValueError:
        # Si ocurre un error al convertir a entero, analizamos qué ingresó el usuario

        # Caso 1: El usuario ingresó un número decimal (tiene punto)
        if entrada_usuario.replace('.', '', 1).isdigit():
            print("Error: Has ingresado un número decimal por favor ingresar solo números enteros.")
        
        # Caso 2: El usuario ingresó solo letras (texto)
        elif entrada_usuario.isalpha():
            print("Error: Has ingresado texto por favor ingresar solo números enteros.")
        
        # Caso 3: El usuario ingresó símbolos o caracteres especiales
        elif re.search(r"[^\w\s]", entrada_usuario):
            print("Error: Has ingresado caracteres especiales por favor ingresar solo números enteros.")
        
        # Caso 4: Entrada vacía o espacio en blanco
        elif entrada_usuario.strip() == "":
            print("Este es un campo obligatorio intenta de nuevo.")
        
        # Otro tipo de error (por ejemplo, mezcla de letras y números)
        else:
            print("Error: Entrada no válida. Solo se permiten números enteros.")

# Se asume que el número ingresado es primo
es_primo = True

# Verifica si el número es menor que 2 (por definición, no es primo)
if numero_ingresado < 2:
    es_primo = False
else:
    # Recorre todos los números desde 2 hasta uno antes del número ingresado
    for divisor in range(2, numero_ingresado):
        # Verifica si el número ingresado es divisible exactamente por otro
        if numero_ingresado % divisor == 0:
            es_primo = False  # Si es divisible, no es primo
            break  # Sale del bucle porque ya sabemos que no es primo

# Muestra el resultado al usuario
if es_primo:
    print("Es primo")
else:
    print("No es primo")
