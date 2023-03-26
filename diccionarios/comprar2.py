# Desarrollado por ChatGPT

'''Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra, mas el IVA y el coste total , con el siguiente formato

# Lista de la compra	
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# ...	...
# Total	Coste'''


# Creamos un diccionario vacío para la cesta
cesta = {}

# Pedimos al usuario los artículos y sus precios
while True:
    # Pedimos al usuario el artículo y su precio
    articulo = input("Introduce el nombre del artículo (o 'fin' para terminar): ")
    if articulo == "fin":
        break
    precio = float(input("Introduce el precio del artículo: "))
    
    # Añadimos el artículo y su precio a la cesta
    cesta[articulo] = precio

# Calculamos el coste total y el IVA
total = sum(cesta.values())
iva = total * 0.19

# Mostramos la lista de la compra
print("\nLista de la compra")
for articulo, precio in cesta.items():
    print(f"{articulo}\t{precio}")

# Mostramos el coste total y el IVA
print(f"Total\t{total:.2f}")
print(f"IVA\t{iva:.2f}")
print(f"Coste\t{total + iva:.2f}")

