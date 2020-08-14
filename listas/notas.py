# Programa en el cual reciba como entradas la siguiente información: Código del Estudiante, Nombre del Estudiante, Nombre de la Materia y Tres Notas de 1.0 a 5.0. Con esta información el programa debe calcular la nota definitiva (promedio) y determinar si el estudiante aprueba o no la materia (Definitiva mayor a 4.0). Debe imprimir como salidas el nombre, el código, la materia y si aprobó o no.

suma = 0

print('')
codigo = int(input('Codigo del estudiante: '))
nombre = (input('Nombre del estudiante: '))
asignatura = (input('Nombre de la asignatura: '))
notas = ([])
print('')

# Rellenar la lista
for x in range(3):
    noticas = int(input('Digite la nota # {}: '.format(x+1)))
    notas.append(noticas)
print('')

# Sumar las notas
for i in notas:
    suma = suma + i
    promedio = suma / 3    

if promedio >= 40:
    print('\n{0}, su codigo es: {1}, la asignatura es: {2}, Si aprobo,'.format(nombre,codigo,asignatura))
elif promedio <=39:
    print('\n{0}, su codigo es: {1}, la asignatura es: {2}, NO aprobo,'.format(nombre,codigo,asignatura))




