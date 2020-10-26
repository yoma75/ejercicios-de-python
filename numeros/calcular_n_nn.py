# Solicitar al Usuario un Número n y Calcular n + nn + nnn
# Ejemplo: n = 3 entonces: 3 + 33 + 333 = 369

n = int(input('\nEscriba el valor de n: '.upper()))

nn = int(f'{n}{n}')
nnn = int('%s%s%s'%(n,n,n)) # otra forma de hacerlo
suma = n + nn + nnn

print(f'La suma de {n} + {nn} + {nnn} es: {suma}')

