# Desarrollado con chatGPT: escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de libras y muestre por pantalla el precio de ese número de libras de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	    Precio
# Plátano	 1.350
# Manzana	 800
# Pera	     850
# Naranja	 700

'''Este programa primero define el diccionario frutas_precios que contiene los precios de las frutas. Luego, le pregunta al usuario qué fruta y cuántas libras desea comprar. Luego verifica si la fruta está en el diccionario utilizando el método .get(), que devuelve None si la clave no está presente. Si la fruta no está en el diccionario, se le informa al usuario. De lo contrario, el programa calcula el precio total y lo muestra al usuario'''


# Definir el diccionario de precios
frutas_precios = {
    "Plátano": 1.350,
    "Manzana": 800,
    "Pera": 850,
    "Naranja": 700
}

# Preguntar al usuario por una fruta y el número de libras
fruta = input("\n¿Qué fruta quieres comprar? ")
libras = float(input("¿Cuántas libras quieres comprar? "))


# Obtener el precio de la fruta del diccionario (si está disponible)
precio = frutas_precios.get(fruta)


# Verificar si la fruta está en el diccionario
if precio is None:
    print(f"Lo siento, no tenemos {fruta}.")
else:
    # Calcular el precio total
    total = precio * libras


    # Mostrar el precio total al usuario
    print(f"{libras} libras de {fruta} cuestan {total} pesos.\n")
