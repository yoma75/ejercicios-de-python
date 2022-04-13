# Pregunta su nombre al usuario y responde:
# Su inicial
# La cantidad de letras
# La última letra
# Su nombre en mayúsculas
# Su nombre al revés
# La cantidad de vocales que contiene

nombre = input('Escribe tu primer nombre: '.upper())

print(f'Letra inicial: {nombre[0]}')
print(f'Cantidad de letras: {len(nombre)}')
print(f'Última letra: {nombre[-1]}')
print(f'En mayúsculas: {nombre.upper()}')
print(f'Al reves: {nombre[::-1]}')

cantidadVocales = 0
for x in nombre.upper():
  if ((x == 'A') or (x == 'E') or (x == 'U') or (x == 'I') or (x == 'O')):
    cantidadVocales += 1

print(f'Cantidad de vocales: {cantidadVocales}\n')
