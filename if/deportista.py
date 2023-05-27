# Programa para determinar si un deportista es aceptado en el equipo de baloncesto de Bogotá. Las condiciones para ser aceptado son: 
# a) La edad debe ser menor o igual a 18 años 
# b) La estatura debe ser mayor a 180 cm 
# c) El peso debe ser menor o igual a 80 kg

# Si el aspirante cumple las 3 condiciones aceptarlo si no rechazarlo.

nombre = input('Cual es tu nombre: ')
edad = int(input('Tu edad: '))
estatura = float(input('Tu estatura: '))
peso = int(input('Tu peso corporal: '))

if edad <= 18 and estatura >= 1.80 and peso <= 80:
    print('ACEPTADO, cumples con las condiciones exigidas')
else:
    print('RACHAZADO, no cumples con las condiciones exigidas')
