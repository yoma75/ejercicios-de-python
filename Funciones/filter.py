# FILTER: función para filtrar resultados según una condición

def positivo(numero):
  if (numero > 0):
    return True
  else:
    return False

print(positivo(5))
print(positivo(-3))


# Listar numeros positivos
numeros = [24, -5, -2, 12, 68, -9, 57]
filtro = filter(positivo, numeros)

# Convertirlo a una lista
resultado = list(filtro)
print(f'Los numeros positivos son: {resultado}')



