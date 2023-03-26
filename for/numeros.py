# Escribir un programa que pida al usuario un número entero positivo  
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input('\nDigite un numero positivo: '.upper()))  # 8

for i in range(1, numero+1, 2):
    print(i, end=', ')  # 1, 3, 5, 7,