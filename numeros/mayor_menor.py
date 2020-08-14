# Ordenar Tres Números de menor a mayor sin Usar Condicionales ni Ciclos

x = int(input('Escriba el primer numero: '))
y = int(input('Escriba el segundo numero: '))
z = int(input('Escriba el tercer numero: '))

a = min(x, y, z) # min: minimo funcion integrada en python
c = max(x, y, z) # max: maximo
b = (x + y + z) - a - c

# 1 2 3
# a = 1
# c = 3
# b = (1 + 2 + 3) - 1 - 3
# b = 6 - 1 - 3 = 2

print(f'Los numeros ordenados son: {a}, {b} y {c}')

