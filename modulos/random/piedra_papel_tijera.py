# Juego de piedra, papel y tijera

import random


def jugar():
  usuario = input("Escoge uan opcion: 'pi': piedra, 'pa' : papel y 'ti' : tijera.\n").lower()
  computadora = random.choice(['pi', 'pa', 'ti'])  # choice: escoge una opcion de una lista

  if usuario == computadora:
    return "!Empate¡"

  if gano_el_jugador(usuario, computadora):
    return 'Ganaste'  
  return 'Perdiste'


def gano_el_jugador(jugador, oponente):
  # Retornar True (verdadero) si gana el jugador
  # Piedra gana a tijera (pi > ti)
  # Tijera gana a papel (ti > pa)
  # Papel gana a piedra (pa > pi)

  if ((jugador == 'pi' and oponente == 'ti') 
      or (jugador == 'ti' and oponente == 'pa') 
      or (jugador == 'pa' and oponente == 'pi')):
      return True
  else:
    return False


print(jugar())
