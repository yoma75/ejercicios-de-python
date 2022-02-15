# Dicen que un año en un humano es equivalente a 7 años de vida de los perros. Escribe una función llamada edad_perruna que reciba dos parámetros: nombre y edad. La función debe calcular la edad en años perrunos y retornar la siguiente cadena de texto (string): ", tienes en años perrunos!".


def edad_perruna(nombre, edad):
  years_perrunos = edad * 7
  return f'{nombre} tienes en años perrunos: {years_perrunos} años'

print(f'{edad_perruna("Pedro", 20)}')  # 140
print(f'{edad_perruna("Maria", 8)}')   # 56
print(f'{edad_perruna("Alex", 45)}\n') # 315
