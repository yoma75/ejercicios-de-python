# Escribe un programa que le pida al usuario ingresar un número, luego le pide un segundo número, e imprima en la consola la suma de los dos números que ingresó el usuario.

def suma():
  a = int(input('Digite un número: '))
  b = int(input('Digite otro número: '))
  return print(f'La suma entre {a} y {b} es: {a + b}\n')

suma()
