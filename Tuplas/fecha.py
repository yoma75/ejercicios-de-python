# Mostrar la Fecha de un Evento Almacenada en una Tupla

fecha_evento = (2020, 6, 14)

print(type(fecha_evento))
print()  # <class 'tuple'>

print(f'El evento fue creado el dia: {fecha_evento}\n')
# El evento fue creado el dia: (2020, 6, 14)

print('El evento fue creado el dia: %i/%i/%i' %fecha_evento)
# El evento fue creado el dia: 2020/6/14


''' El mensaje contiene una cadena de texto y una serie de valores numéricos que se formatean utilizando el operador %.

La parte %i/%i/%i dentro de la cadena de texto es conocida como una cadena de formato y especifica que se espera que se proporcionen tres valores enteros para reemplazar cada uno de los tres %i en orden. Estos valores serán tomados de la variable fecha_evento'''
