# Leer un número y escribir el valor absoluto del mismo. 
# Si es positivo queda positivo y si es negativo queda positivo

import math
print('---------- valor absoluto de un numero ----------'.upper())
print('')

numero = int(input('Escriba un numero positivo o negativo: '))

y = math.fabs(numero)
print(y)

# .fabs: Return the absolute value of the float


