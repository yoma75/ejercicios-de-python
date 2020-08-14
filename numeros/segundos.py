# Convertir Todas las Unidades de Tiempo en Segundos

dias = int(input('Escriba la cantidad de dias: '))
horas = int(input('Escriba la cantidad de horas: '))
minutos = int(input('Escriba la cantidad de minutos: '))
segundos = int(input('Escriba la cantidad de segundos: '))

# un dia tiene 24 horas, una hora 60 minutos y un minuto 60 segundos
segundos += dias * 24 * 60 * 60 
segundos += horas * 60 * 60
segundos += minutos * 60

print(f'Total: {segundos} segundos')
