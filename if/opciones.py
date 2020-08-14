# Programa que muestre un menú que tenga las siguientes opciones:

# 1. Pasa o no la materia? 
# 2. Es mayor o menor de edad? 
# Caso 1: Solicitar 3 notas y determinar si el promedio es mayor a 3.0, en ese caso el estudiante pasa.
# Caso 2: Se debe solicitar el año de nacimiento y el año actual y determinar si es o no mayor de edad.

notas = list([])
YEAR_ACTUAL = 2020
sumar_notas = 0

print('')
nombre= input('Nombre del estudiante: '.upper())
print('')

print('Que desea saber'.upper())
print('1. Pasa o no ma materia')
print('2. Es mayor o menor de edad')
opc = int(input('Escoja una opcion: '))
print('')

if opc == 1:
    for x in range(3):
        noticas = int(input(f'Nota # {x+1}: '))
        notas.append(noticas)
    print('')

    for i in notas:
        sumar_notas = sumar_notas + i
        promedio_notas = round(sumar_notas / len(notas))
    
    if promedio_notas >= 30:
        print(f'{nombre} usted APROBO la asignatura de Algebra. Nota: {promedio_notas}')
    else:
        print(f'{nombre} usted NO APROBO la asignatura de Algebra. Nota: {promedio_notas}')

elif opc == 2:
    year_birth = int(input('Escriba su año de nacimiento: '))
    respuesta = YEAR_ACTUAL - year_birth

    if respuesta >= 18:
        print(f'{nombre} tiene: {respuesta} años y es mayor de edad')
    else:
        print(f'{nombre} tiene: {respuesta} años y es menor de edad')

