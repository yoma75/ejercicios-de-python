# Imprimir el calendario para un año y mes especifico:

import calendar

print()
year = int(input('Escriba el año: '.upper()))
mes = int(input('Escriba el mes en numero: '.upper()))
print()

# funcion month disponible en el modulo calendar
print(calendar.month(year, mes))
