# Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

opcionMes = int(input('\nIngresa el número del mes: '))

print(f'El número {opcionMes} corresponde al mes de: {meses[opcionMes-1]}\n')