# calcular la suma de los dígitos de un número aleatorio de tres dígitos


# la función random () genera un número fraccionario aleatorio de 0 a 1
from random import random

# Cuando el numero es multiplicado por 900 un numero aleatorio es obtenido de 0 a 899
# Si le agregas 100 a esto, obtienes un numero de 100 a 999
n = random() * 900 + 100

# se descarta la parte fraccionaria, se muestra el número
n = int(n)
print(n)

# el primer dígito (el más significativo) del número se extrae dividiéndolo por 100
a = n // 100

b = (n // 100) % 10
c = n % 10

print(a + b + c)

