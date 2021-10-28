# Generar los n Primeros Números Pares Positivos

print()
numero = int(input('Digite hasta que numero desea ver los pares de N: '.upper()))

for x in range(numero +2):
    if x % 2 == 0:
        print(x, end=' ')


# Sumar todos los numeros pares de 0 a 100:
suma = 0

for x in range(0, 102):
    if (x % 2 == 0):
        suma += x

print()
print(f'\nLa suma de 0 a 100 en números pares es: {suma}'.upper())
