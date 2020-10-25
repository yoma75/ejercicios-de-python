# Leer un número y escribir el valor absoluto del mismo. 
# Si es positivo queda positivo y si es negativo queda positivo

import math
print('\n---------- valor absoluto de un numero ----------'.upper())

numero = int(input('\nEscriba un número positivo o negativo: '))

y = math.fabs(numero)
print(y)

# .fabs: Return the absolute value of the float


