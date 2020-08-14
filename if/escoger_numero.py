# Programa que permita ingresar un número cualquiera y luego mostrar el siguiente menú:

# 1. Determinar si es positivo o negativo 
# 2. Determinar si es par o impar

# El programa debe realizar las operaciones que el usuario seleccione del menú

print()
numero = int(input('Digite un numero entero: '))

print()
print('1. Determinar si es positivo o negativo')
print('2. Determinar si es par o impar')
opc = int(input('Escoja la opcion: '))
print('')

if opc == 1:
    if numero >= 0:
        print('Es positivo')
    else:
        print('Es negativo')

if opc == 2:
    if numero % 2 == 0:
        print('Es par')
    else:
        print('Es impar')




