# Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 9%.

import pandas as pd

inicio = int(input('Introduce el año inicial: '))
fin = int(input('Introduce el año final: '))
ventas = {} # es un diccionario

for x in range(inicio, fin+1):
    ventas[x] = float(input('Introduce las ventas del año '+ str(x) +': '))

ventas = pd.Series(ventas)
print()
print('Ventas\n', ventas)

print()
print('Ventas con descuento\n', ventas*0.9)

