# se realizan dos 'mezclas' shuffle() antes de que se obtenga el elemento.

import random

colores = ['rojo', 'verde', 'amarillo']

random.shuffle(colores)
print(f'Mezcla1: {colores}')

random.shuffle(colores)
print('mezcla2', colores)
print(colores[random.randint(0,2)])


