# Dada una lista de números y un número objetivo, escribe un programa que cuente cuántos elementos de la lista son mayores que el número objetivo.

numeros = [23, 45, 68, 12, 5, 98, 7]
numero_objetivo = 25
contador = 0

for x in numeros:
    if x >= numero_objetivo:
        contador = contador + 1

print(numeros)
print(f'En la lista existen {contador} numeros mayores a {numero_objetivo}\n')
# En la lista existen 3 numeros mayores a 25
