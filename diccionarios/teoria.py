animalitos = {
    'leon':'salvaje',
    'rana':'anfibio',
    'jirafa':'hervivora',
    'perro':'domestico',
    'zancudo':'insecto',
    'calamar':'crustaceo'
}

# Encontrar el value de una determinada key
print('')
print(animalitos['rana']) 

# Cantidad de pares en el diccionario
print(len(animalitos))

# método values: retorna los valores como una lista
valores = list(animalitos.values())
print(f'Valores: {valores}')

# Metodo keys: retorna las llaves
valores = list(animalitos.keys())
print(f'Keys: {valores}')

# Eliminar dato 
del(animalitos['zancudo'])
print(f'Eliminar zancudo: {animalitos}')

# Modificar valor
animalitos['jirafa'] = 'muy alta'
print(animalitos)


