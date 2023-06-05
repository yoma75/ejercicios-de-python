# Calcular la longitud de la hipotenusa de un triangulo rectangulo

# sqrt: raiz cuadrada
from math import sqrt

ab = float(input('Escriba el valor del vértice AB: '))
bc = float(input('Escriba el valor del vértice BC: '))

hipotenusa = sqrt(ab**2 + bc**2)

print(f'La longitud de la hipotenusa es: {hipotenusa}')

