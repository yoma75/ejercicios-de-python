# Concatenar dos listas

animals = ['bear', 'tiger', 'shark']
colors = ['black', 'yellow', 'blue']

animals.extend(colors)
print(f'\n{animals}')  # ['bear', 'tiger', 'shark', 'black', 'yellow', 'blue']
print(f'{len(animals)} elementos')  # 6 elementos

# obtener el ultimo elemento
print(animals[-1])  # blue

