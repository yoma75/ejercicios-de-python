# Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

numeros = [-12, 84, 13, 20, -33, 101, 9, 123, 54, 2, 1]

def separar(lista):
    lista.sort()
    pares = []
    impares = []
    
    for n in lista:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separar(numeros)
print('Los numeros pares son: {}'.format(pares))
print('y los numeros impares son: {}'.format(impares))
