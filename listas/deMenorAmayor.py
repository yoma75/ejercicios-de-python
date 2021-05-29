# preguntar al usuario los números ganadores de la lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

loteria = []

for x in range(6):
  loteria.append(int(input('Introduzca un número ganador: ')))

loteria.sort()
print(f'Los números ganadores son: {loteria} felicitaciones al ganador\n')
