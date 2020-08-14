# Calcular el Volumen de una Esfera a partir del Radio Dado

from math import pi

print()

radio = float(input('radio de la esfera: '.upper()))
volumen = 4/3 * pi * radio ** 3

print('El volumen de la esfera es {r:1.2f} unidades cubicas'.format(r=volumen))


