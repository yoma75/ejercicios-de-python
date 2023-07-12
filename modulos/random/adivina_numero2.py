import random

intentos_realizados = 0
nombre = input('Como te llamas: ')
numero = random.randint(1, 20)

print(f'\nBueno {nombre}, estoy pensando un número entre 1 y 20')

while intentos_realizados < 6:
    estimacion = int(input('Intenta adivinar el número: '))
    intentos_realizados += 1

    if estimacion < numero:
        print('Tu número estimado es muy bajo\n')
    elif estimacion > numero:
        print('Tu número estimado es muy alto\n')
    else:
        print(f'\nBuen trabajo {nombre}, has adivinado, tuviste {intentos_realizados} intentos realizados')
        break
else:
    numero = int(numero)
    print(f'\nFallaste, el número que pensé fue {numero}')
