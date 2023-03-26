# Creado con chatGPT

'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''


# Creamos un diccionario vacío para guardar la información de la persona
persona = {}

# Pedimos al usuario la información de la persona
while True:
    clave = input("Introduce la clave de la información (o 'fin' para terminar): ")
    if clave == "fin":
        break
    valor = input(f"Introduce el valor de '{clave}': ")
    
    # Añadimos la clave y el valor al diccionario de la persona
    persona[clave] = valor
    
# Imprimimos el contenido actual del diccionario
print('\n', persona)
