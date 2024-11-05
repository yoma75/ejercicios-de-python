# Cambiar aguila por halcon

animales = ['perro', 'araña', 'aguila', 'delfin', 'gato']
cambioAnimal = [x if x != 'aguila' else 'halcon' for x in animales]

print(animales)      # ['perro', 'araña', 'aguila', 'delfin', 'gato']
print(cambioAnimal)  # ['perro', 'araña', 'halcon', 'delfin', 'gato']


'''
1. x if x != 'aguila': Si el elemento x no es igual a 'aguila', se mantiene el valor original x.
2. else 'halcon': Si el elemento x es igual a 'aguila', se reemplaza por 'halcon'.
'''