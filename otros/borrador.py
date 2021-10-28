hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

# encuentra el número de horas ocultos en los minutos y actualiza las horas

if (dura >= 59):
    hora += 1

if (hora >= 23):
  hora = 0

variable = dura % 59 
min = variable + min

# corrige los minutos para que estén en un rango de (0..59)
# corrige las horas para que estén en un rango de (0..23) 

print(hora, ":", min, sep='')

