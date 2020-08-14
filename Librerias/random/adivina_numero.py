# Adivinar el numero que escoge la computadora:

import random

intentos_Realizados = 0

print('')
nombre = input('Como te llamas: ')
numero = random.randint(1, 20) # La función randint() es parte del módulo random
print('Bueno {}, estoy pensando un numero entre 1 y 20'.format(nombre,))

while intentos_Realizados < 6:
    print('')
    estimacion = int(input('Intenta adivinar el numero: '))
    intentos_Realizados = intentos_Realizados + 1

    if estimacion < numero:
        print('Tu numero estimado es muy bajo')
    elif estimacion > numero:
        print('Tu numero estimado es muy alto')
    elif estimacion == numero:
        break

if estimacion == numero:
    print('')
    intentos_Realizados = int(intentos_Realizados)
    print(f'Buen trabajo {nombre} has adivinado, tuviste {intentos_Realizados} intentos realizados')

print('')
if estimacion != numero: # Diferente a 
    numero = int(numero)
    print(f'Fallaste, el numero que pense fue {numero}')

