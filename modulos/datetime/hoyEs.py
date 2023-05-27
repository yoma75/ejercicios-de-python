# Para obtener la fecha y hora actuales, necesitamos usar la biblioteca de fecha y hora
from datetime import datetime

# La función now devuelve la fecha y hora actual
today = datetime.now()

# uso de funciones de día, mes, año, hora, minuto y segundo
# para mostrar solo una parte de la fecha
# Todas estas funciones devuelven enteros
# Conviértelos en cadenas antes de concatenarlos a otra cadena
print(f'Day: {(today.day)}')
print(f'Month: {(today.month)}')
print(f'Year: {(today.year)}')

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))

