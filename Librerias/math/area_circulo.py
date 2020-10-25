# Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio. 

import math

def area_circulo(radio):
    return(radio ** 2) * math.pi

print('\nEl área del circulo es de: {r:1.1f} centimetros'.format(r=area_circulo(5)))
print('El área del circulo es de: {r:1.1f} centimetros'.format(r=area_circulo(15)))
print('El área del circulo es de: {r:1.1f} centimetros'.format(r=area_circulo(23)))
print('El área del circulo es de: {r:1.1f} centimetros'.format(r=area_circulo(14)))
print('El área del circulo es de: {r:1.1f} centimetros'.format(r=area_circulo(56)))
