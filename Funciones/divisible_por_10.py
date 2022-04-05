# Escribe una función llamada divisible_por_10 que reciba un parámetro num que retorne True si num es divisible por 10 y False de lo contrario.

def divisible_por_10(num):
  if (num % 10 == 0):
    return True
  else:
    return False


print(divisible_por_10(100))  # True
print(divisible_por_10(1980)) # True
print(divisible_por_10(38))   # False
