# Almacena en una lista los numeros del 1 al 10 y mostrarlos en orden inverso separados por guiones
# Le da la vuelta a la lista actual

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()
print(numeros)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


for x in numeros:
    print(x, end=" - ")  # 10 - 9 - 8 - 7 - 6 - 5 - 4 - 3 - 2 - 1 -    


# Las cadenas no tienen el método .reverse() pero podemos simularlo haciendo unas conversiones:

lista = list("Hola mundo")
lista.reverse()
cadena = "".join(lista)
print(f'{cadena}')  # odnum aloH
