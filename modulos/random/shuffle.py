# se realizan dos 'mezclas' shuffle() antes de que se obtenga el elemento.

import random

colors = ['red', 'green', 'yellow']

random.shuffle(colors)
print(f'Mezcla1: {colors}')  # Mezcla1: ['green', 'yellow', 'red']

random.shuffle(colors)
print('mezcla2', colors)  # mezcla2 ['yellow', 'red', 'green']
print(colors[random.randint(0,2)])  # red
