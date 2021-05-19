# Crear la función 'pares' que devuelva un array de números pares entre 2 valores pasados como parametros a la función (valor_inicial, valor_final)
# Utilizar la función pares con los números 1 y 30
# Utilizar la función pares con los números 2 y 40

import numpy as np

def pares(inicial, final):
  if (inicial % 2 == 0):
    array = np.arange(inicial,final,2)  # que vaya del inicio al final de 2 en 2
  else:
    inicial += 1  # de lo contrario, al inicio súmele 1 para que sea impar
    array = np.arange(inicial,final,2)
  return array

print(pares(1,30))
print(pares(2,40))





