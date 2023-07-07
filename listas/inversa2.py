# Dada una lista de elementos, crea un programa que genere una nueva lista con los elementos en orden inverso al original.

listaNum = []

for x in range(3):
    num = int(input('Digite un numero: '))
    listaNum.append(num)

print(f'Lista: {listaNum} e inversa: {listaNum[::-1]}')  # Lista: [1, 6, 2] e inversa: [2, 6, 1]
