# obtener mediante filter los números pares de la lista

numbers = [1,2,3,4,5,6,7,8,9,10]

def par(numero):
  if (numero % 2) == 0:
    return True
  else:
    return False

print(par(3))  # False
print(par(6))  # True

print(list(filter(par, numbers)))  # [2, 4, 6, 8, 10]

# En una sola línea de código
print(list(filter(lambda numero : numero % 2 == 0, numbers)))  # [2, 4, 6, 8, 10]
