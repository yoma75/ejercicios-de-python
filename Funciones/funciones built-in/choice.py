# elegir un elemento de una secuencia aleatoriamente
# La secuencia puede ser una cadena, un rango, una lista, una tupla o cualquier otro tipo de secuencia

import random

numeros = [189, 248, 745, 197, 895, 369]
resultado = random.choice(numeros)
print(resultado)



# Otra opción es usar la función random.sample() que devuelve una lista de elementos al azar sin repetición. 

import random
secuencia = ["a", "b", "c", "d", "e"]
elementos = random.sample(secuencia, 2)
print(elementos)

