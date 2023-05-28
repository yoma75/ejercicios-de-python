'''sleep puedes pausar un programa durante un tiempo determinado y hacer que siga ejecutándose automáticamente una vez transcurrido el periodo de espera. Con él, los usuarios pueden, por ejemplo, sacar tiempo para leerse unas instrucciones, o crear su propia cuenta atrás digital.'''

from time import sleep

countdown = [4, 3, 2, 1, 0]

for x in countdown:
  print(x)
  sleep(2)  # espera 2 segundos
print('He terminado')
