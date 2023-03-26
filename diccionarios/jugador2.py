# DESARROLLADO CON CHATGPT: con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

'''En primer lugar, se define el diccionario jugadores con los números y nombres de los jugadores.

Después, se pide al usuario que introduzca un número entre el 1 y el 18 (los números de los jugadores). El número introducido se convierte a entero con la función int().

A continuación, se comprueba si el número introducido está en el diccionario utilizando el operador in. Si está en el diccionario, se busca el jugador correspondiente utilizando el número como clave y se almacena en la variable jugador. Finalmente, se imprime el jugador utilizando la función print() y una cadena formateada.

Si el número introducido no está en el diccionario, se muestra un mensaje de error utilizando la función print().'''

# Definimos el diccionario de jugadores
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

# Pedimos al usuario un número
numero = int(input("Introduce un número del 1 al 18: "))

# Buscamos el jugador correspondiente en el diccionario
if numero in jugadores:
  jugador = jugadores[numero]
  print(f"El jugador con el número {numero} es: {jugador}")
else:
  print("El número introducido no es válido")
