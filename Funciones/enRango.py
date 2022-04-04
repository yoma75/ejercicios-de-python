 # Escribe una función llamada en_rango que reciba tres parámetros: num, inferior, superior. La función debe retornar True si num es mayor o igual a inferior y menor a superior. De lo contrario debe retornar False.

# print(en_rango(5, 1, 10)) # True
# print(en_rango(5, 6, 10)) # False
# print(en_rango(1, 1, 10)) # True
# print(en_rango(10, 1, 10)) # False


def en_rango(num, inferior, superior):
  if ((num >= inferior) and (num < superior)):
    return True
  else:
    return False


print(en_rango(5, 1, 10))  # True
print(en_rango(5, 6, 10))  # False
print(en_rango(1, 1, 10))  # True
print(en_rango(10, 1, 10)) # False