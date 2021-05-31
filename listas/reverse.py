# Almacena en una lista los numeros del 1 al 10 y mostrarlos en orden inverso separados por comas

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()

for x in numeros:
    print(x, end=", ")  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    
