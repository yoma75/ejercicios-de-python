# Escribe una función llamada propina que reciba dos números: total y porcentaje. La función debe retornar el valor de la propina.

# print(propina(100, 50)) # 50
# print(propina(200, 10)) # 20
# print(propina(5000, 90)) # 4500


def propina(total, porcentaje):
  return f'El valor de la propina es: {int(total * porcentaje / 100)}'

print(propina(100, 50))
print(propina(200, 10))
print(propina(5000, 90))