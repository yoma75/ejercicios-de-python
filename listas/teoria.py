import random

# Elegir un elemento aleatoriamente: choice()
miles = [2345, 8723, 9567, 1865, 4095]
print(f'\n{random.choice(miles)}')

# Modificar un elemento
miles[3] = 4
print(miles)  # [2345, 8723, 9567, 4, 4095]

