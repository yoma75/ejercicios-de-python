# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

INTERESES = 0.04

dinero = int(input('Digite la cantidad de dinero a depositar: '))

first_year = dinero * (1 + INTERESES)
second_year = round(first_year * (1 + INTERESES))
third_year = round(second_year * (1 + INTERESES))
tota_ahorrado = round(dinero + first_year + second_year + third_year)

print('El primer año de ahorro fue de: {}'.format(first_year))
print('El segundo año de ahorro fue de: {}'.format(second_year))
print('El tercer año de ahorro fue de: {}'.format(third_year))
print('El dinero total durante los tres años fue de: $ {}'.format(tota_ahorrado))