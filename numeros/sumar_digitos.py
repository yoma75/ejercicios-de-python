# Sumar los Dígitos Integrales de un Número Entero
# Ejemplo: 1237: 13 (1+2+3+7)

# El numero capturado se pàsa a una lista
# Cada posicion de la lista sera un caracter


numero = input('Digite un numero entero positivo: ') # 1237
lista_digitos = list(numero)

print(lista_digitos) # ['1', '2', '3', '7']

# Convertir lista_digitos que esta como string a enteros
# [lista de compresion de cada caracter]
lista_digitos = [int(x) for x in lista_digitos] 
print(lista_digitos) # [1, 2, 3, 7]

suma = sum(lista_digitos)
print(f'La suma es: {suma}')


# Forma resumida
sumita = sum([int(x) for x in numero])
print(f'La sumita es: {sumita}')

