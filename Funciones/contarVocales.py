# Contar las vocales que se encuentren en el texto

def contar_vocales(cadena):
  vocales = "aeiouAEIOU"
  contador = 0

  for x in cadena:
    if x in vocales:
      contador += 1
  
  return contador

cadena_usuario = input("Por favor, ingresa una cadena de texto: ")
numero_vocales = contar_vocales(cadena_usuario)  # llama la funcion

print(f"El número de vocales en la cadena es: {numero_vocales}")
