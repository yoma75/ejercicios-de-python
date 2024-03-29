# Map: aplica una función a cada uno de los elementos de una lista

def multiplicar(numero):
  return numero * 2

print(multiplicar(2))  # 4

numbers = [25,41,60,34]
mapeo = map(multiplicar, numbers)
resultado = list(mapeo)
print(resultado)  # [50, 82, 120, 68]

# En una sola línea 
print(f'En una sola línea: {list(map(multiplicar, numbers))}\n')  # [50, 82, 120, 68]

# Con una función lambda sin nombre:
print(f'Con función lambda: {list(map(lambda numero : numero * 2, numbers))}\n')  
# [50, 82, 120, 68]
