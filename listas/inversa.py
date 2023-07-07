# Dada una lista de elementos, crea un programa que genere una nueva lista con los elementos en orden inverso al original.

listaNum = []

for x in range(3):
    num = int(input('Digite un numero: '))
    listaNum.append(num)

print(f'lista {listaNum}')  # lista [87, 3, 9]

listaNum.reverse()
print(f'inversa {listaNum}')  # inversa [9, 3, 87]
