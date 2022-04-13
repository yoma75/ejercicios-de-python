# Pide al usuario un número entero del 1 al 12 y escribe el nombre del mes correspondiente (1=enero, 12=diciembre).

monthsOfYear = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

number = int(input("Dime el número de mes (1 a 12): "))

print(f'El número {number} corresponde al mes de: {monthsOfYear[number-1]}\n')

