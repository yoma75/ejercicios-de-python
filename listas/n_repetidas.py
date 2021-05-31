# Crear una Subcadena de n Caracteres Replicada n Cantidad de Veces
# árbol => ar captura los dos primeros caracteres y los multiplica las veces requeridas

cadena=input('Introduzca cadena:')
numero=int(input('Introduzca numero de caracteres de la subcadena :'))

cadena2=cadena[:numero]*numero
print(cadena2)

