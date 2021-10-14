# insert: agrega un ítem a la lista en un índice específico
# sintaxis: variable.insert(index, valor_a_agregar)

numeritos = [25, 8, 12, 38]
numeritos.insert(2,457)
print(numeritos)  # [25, 8, 457, 12, 38]


# Última posición en una lista con len():
# Si la posición esta fuera de rango añade el elemento al final de la lista

numeros = [23, 78, 95, 41]
ultima_posicion = len(numeros)
numeros.insert(ultima_posicion, 777)
print(f'{numeros}')  # [23, 78, 95, 41, 777]

