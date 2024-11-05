# Concatenar dos listas

animals = ['bear', 'tiger', 'shark']
colors = ['black', 'yellow', 'blue']

animals.extend(colors)
print(f'\n{animals}')  # ['bear', 'tiger', 'shark', 'black', 'yellow', 'blue']
print(f'{len(animals)} elementos')  # 6 elementos

# obtener el ultimo elemento
print(animals[-1])  # blue

# -----------------------------------------------------------------------------------------

# Tambien con el OPERADOR SUMA '+':
decenas = [10, 20, 30]
centenas = [100, 200, 300]
unir = decenas + centenas
print(unir)  # [10, 20, 30, 100, 200, 300]

# -----------------------------------------------------------------------------------------

# Otra forma de unir dos listas es anexando todos los elementos de lista2 a lista1, uno por uno:
lista1 = ['x', 'y', 'z']
lista2 = [1, 2, 3]

for x in lista2:
  lista1.append(x)

print(lista1)  # ['x', 'y', 'z', 1, 2, 3]
