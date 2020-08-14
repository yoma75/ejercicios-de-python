# Comprobar si Todos los Elementos de una Lista Cumplen una Condición

numeros = [7, 3, 2, 5, 11]

# Todos los numeros son mayor que 1
print(all(x > 1 for x in numeros)) # True

# Todos los numeros son mayor que 5
print(all(x > 5 for x in numeros)) # False

