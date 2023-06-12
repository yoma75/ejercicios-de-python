palabra = list([])

palabra = input('Escriba una palabra: ')

palabra_al_reves = palabra[::-1]

print(f'\nSi a la palabra "{palabra}" que tiene {len(palabra)} caracteres le intercambiamos el primer y ultimo caracter obtenemos: {palabra_al_reves}')
