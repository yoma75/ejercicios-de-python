'''Calcular el Volumen de una Esfera a partir del Radio Dado'''


from math import pi

radio = float(input('\nRadio de la esfera: '.upper()))
volumen = 4/3 * pi * radio ** 3

print('El volumen de la esfera es {r:1.2f} unidades cúbicas'.format(r=volumen))

