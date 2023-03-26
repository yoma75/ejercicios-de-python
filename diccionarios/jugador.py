# Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

jugadores = {
  1 : "Casillas", 
  15 : "Ramos",
   3 : "Pique", 
   5 : "Puyol",
  11 : "Capdevila", 
  14 : "Xabi Alonso",
  16 : "Busquets",
   8 : "Xavi Hernandez",
  18 : "Pedrito", 
   6 : "Iniesta",
   7 : "Villa"
}

numero_jugador = int(input('Digite el número del jugador: '.upper()))

if numero_jugador in jugadores:
  print(f'El nombre del jugador número {numero_jugador} es: {jugadores[numero_jugador]}\n')
else:
  print('Este número no existe\n')
