'''Calcular la duración del año en planetas'''


# Importa la constante pi desde el modulo math
from math import pi

r = float(input("\nRadio de la orbita (millones de kilómetros): "))
v = float(input("Velocidad orbital (km/s): "))

# traducir millones de kilómetros, en solo kilómetros
r = r * 1000000

# Año expresado en segundos, se encuentra la longitud de la circunferencia (2*pi*r), esa es la orbita y se divide por la velocidad
year = 2 * pi * r / v

# Para trasladar los segundos entre dias necesita dividir por 60 y consigue los minutos, entonces multiplica en 60 y consigue las horas y multiplica en 24 para conseguir los dias
year = year / (60 * 60 * 24)

print(f'{round(year)} días\n')

