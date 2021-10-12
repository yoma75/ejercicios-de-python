# sorted: retorna una copia de una lista en forma ordenada, sin alterar la lista original.

numbers = [14, 24, 75, 17, 85, 69, 7]
print(f'desordenada: {numbers}')       # [14, 24, 75, 17, 85, 69, 7]
print(f'ordenada ascendentemente: {sorted(numbers)}')  # [7, 14, 17, 24, 69, 75, 85]
print(f'ordenada descendentemente: {sorted(numbers, reverse=True)}')  # [85, 75, 69, 24, 17, 14, 7]


cats = ['silvestre', 'felix', 'cosmico', 'garfield']
print(f'{sorted(cats)}')  # ['cosmico', 'felix', 'garfield', 'silvestre']
print(f'{sorted(cats, reverse=True)}')  # ['silvestre', 'garfield', 'felix', 'cosmico']

