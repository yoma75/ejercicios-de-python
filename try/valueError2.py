try:
    # Código que quieres ejecutar
    entrada = input("Introduce un número: ")
    num_int = int(entrada)  # Intentamos convertir la entrada a un entero
    print("¡Número válido!")
except ValueError:
    # Este bloque se ejecutará si ocurre un error (por ejemplo, si la entrada no es un número)
    print("No es un valor válido. Introduce un número entero.")
else:
    # Este bloque se ejecutará si el bloque try se ejecuta sin errores
    print(f"El número ingresado es {num_int}.")
finally:
    # Este bloque se ejecutará siempre, independientemente de si hubo errores o no
    print("Fin del programa.")
