# Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la fórmula es: num. pulsaciones = (220 - edad)/10 

print('')

edad= int(input('Digite su edad: '))

pulsa = (220 - edad) / 10

print(f'El numero de pulsaciones que usted tiene por cada 10 sg de ejercicio son: {pulsa} pulsaciones')