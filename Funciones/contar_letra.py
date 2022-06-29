'''Crea una función que reciba una cadena de texto y una letra, y devuelva la cantidad de veces que la letra aparece dentro de la cadena.'''


def cantidadVeces(texto, letra):
  cantidad = 0
  for x in texto:
    if (x == letra):
      cantidad += 1
  return cantidad


print(f"{cantidadVeces('esta es un frase', 'e')} veces")   # 3 veces
print(f"{cantidadVeces('La casa es grande', 'a')} veces")  # 4 veces
print(f"{cantidadVeces('The house is big', 'i')} veces")   # 2 veces
