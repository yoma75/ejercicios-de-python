# count: cuenta el número de veces que aparece un ítem.
# sintaxis: list.count(obj)

cadena = input('\nEscriba una oración o párrafo: ')

cantidad_de_u = cadena.count('u')

if (cantidad_de_u == 1):
    print(f'\nLa cantidad de carácteres "u" es igual a: {cantidad_de_u} vez ')
else:
    print(f'\nLa cantidad de carácteres "u" es igual a: {cantidad_de_u} veces ')

# -----------------------------------------------------------------------------------

ciudades = ['Bogotá', 'Cali', 'Medellín', 'Cali']
print(ciudades.count('Cali'))  # 2
