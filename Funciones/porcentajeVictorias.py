# Escribe una función llamada porcentaje_de_victorias que reciba dos números: victorias y derrotas. La función debe retornar el porcentaje de victorias.


def porcentaje_de_victorias(victorias, derrotas):
  return f'Tus victorias son del {int((victorias/(victorias + derrotas) * 100))} %'

print(porcentaje_de_victorias(5, 5))        # Tus victorias son del 50 %
print(porcentaje_de_victorias(7, 0))        # Tus victorias son del 100 %
print(porcentaje_de_victorias(6000, 4000))  # Tus victorias son del 60 %

