# Generar los n Primeros Números Pares Positivos

print()
numero = int(input('Digite hasta que numero desea ver los pares de N: '.upper()))

for x in range(numero +2):
    if x % 2 == 0:
        print(x)
