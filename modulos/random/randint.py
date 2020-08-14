# En el siguiente ejemplo se realizan cinco "sorteos" y se obtiene, para cada uno de ellos, un regalo de diez posibles.

import random

regalos = ['bicicleta', 'laptop', 'Televisor 42p', 'Juego de cuchillos', 'reloj inteligente',
           'bono de $500 mil', 'lavadora', 'nevera', 'Celular', 'Viaje a Cancun']

print()
for x in range(5):
    regalo = regalos[random.randint(0, 9)]    
    print(f'Sorteo # {x+1} : {regalo}')
