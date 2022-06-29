'''Imprimir el calendario para un año y mes especifico:'''


import calendar

year = int(input('\nEscriba el año: '))
mes = int(input('Escriba el mes en numero: '))

# funcion month disponible en el modulo calendar
print(f'\n{calendar.month(year, mes)}')
