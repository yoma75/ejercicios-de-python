# Adivina el número generado por la computadora en un rango especifico y le diremos al usuario si es mayor, menor o igual

# randint = numero entero aleatorio

import random


def adivina_el_numero(x):  
  print('=======================')
  print(' ¡Bienvenid@ al juego!')
  print('=======================')
  print(f'Tu meta es adivinar el número generado por la computadora\n')

  numero_aleatorio = random.randint(1, x)  # Número aleatorio entre 1 y x

  prediccion = 0

  # Mientras que la prediccion no sea igual (!=) al numero aleatorio
  while prediccion != numero_aleatorio:
    prediccion = int(input(f"Adivina un número entre 1 y {x}: "))

    if prediccion < numero_aleatorio:
      print("Intenta otra vez, este número es muy pequeño")
    elif prediccion > numero_aleatorio:
      print("Intenta otra vez, este número es muy grande")

  print(f"!FELICITACIONES¡ Adivinaste el número {numero_aleatorio} correctamente.")


adivina_el_numero(10)
