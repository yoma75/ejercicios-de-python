'''Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra, mas el IVA y el coste total , con el siguiente formato

# Lista de la compra	
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# ...	...
# Total	Coste'''

carrito_compra = {}
masArticulos = 's'

while masArticulos == 's':
    articulo = input('\nIntroduce el articulo: ')
    precio = float(input(f'Digite el precio del {articulo}: '))
    carrito_compra[articulo] = precio
    print()
    masArticulos = input('Quieres añadir mas articulos s/n: ')

costo = 0
print('\nLista de la compra'.upper())

for articulo, precio in carrito_compra.items():
    print(f'{articulo} \t:\t {precio}') # \t: tabulador
    costo += round(precio)

print(f'\nSubtotal: {costo}'.upper())
print(f'+ 19% IVA\t:\t{costo * 0.19}')

totalFinal = costo + (costo * 0.19)
print(f'TOTAL A PAGAR\t:\t{totalFinal}')

