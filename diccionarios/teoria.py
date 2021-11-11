animalitos = {
    'león':'salvaje',
    'rana':'anfibio',
    'jirafa':'herbívora',
    'perro':'domestico',
    'zancudo':'insecto',
    'calamar':'crustáceo'
}

# Encontrar el value de una determinada key
print('')
print(animalitos['rana'])  # anfibio 

# Cantidad de pares en el diccionario
print(len(animalitos))  # 6

# método values: retorna los valores como una lista
valores = list(animalitos.values())
print(f'Valores: {valores}')  # Valores: ['salvaje', 'anfibio', 'herbívora', 'domestico', 'insecto', 'crustáceo']

# Método keys: retorna las llaves
valores = list(animalitos.keys())
print(f'Keys: {valores}')  # Keys: ['león', 'rana', 'jirafa', 'perro', 'zancudo', 'calamar']

# Eliminar dato 
del(animalitos['zancudo'])
print(f'Eliminar zancudo: {animalitos}')  # Eliminar zancudo: {'león': 'salvaje', 'rana': 'anfibio', 'jirafa': 'herbívora', 'perro': 'domestico', 'calamar': 'crustáceo'}

# Modificar valor
animalitos['jirafa'] = 'muy alta'
print(animalitos)  # {'león': 'salvaje', 'rana': 'anfibio', 'jirafa': 'muy alta', 'perro': 'domestico', 'calamar': 'crustáceo'}

