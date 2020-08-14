# Calcular la suma desde 1 hasta N numeros:

print()
numero = int(input('Digite hasta que numero desea sumar: '.upper()))

suma = sum(range(1, numero+1))
print(f'La suma de 1 hasta {numero} es: {suma}')

