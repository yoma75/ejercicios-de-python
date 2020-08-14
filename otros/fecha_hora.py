# Mostrar la fecha y hora actual del sistema:

import datetime as dt

#          objeto.funcion
ahora = dt.datetime.now()
print()
print(ahora)

print()
print(ahora.strftime('%d/%m/%Y %H:%M:%S')) # formatea fecha y hora


