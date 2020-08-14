palabra = list([])

palabra = input('Escriba una palabra: ')

primera_letra = palabra[0]
ultima_letra = palabra[len(palabra)-1]
nueva_palabra = list(palabra)

nueva_palabra[0] = ultima_letra
nueva_palabra[len(nueva_palabra)-1] = primera_letra

print('')
print(f'Si a la palabra {palabra} que tiene {len(palabra)} caracteres le intercambiamos el primer y ultimo caracter obtenemos: {nueva_palabra}')



