# Programa el cual permita ingresar los valores de temperatura de cada día durante una semana. El programa debe calcular la temperatura promedio y luego mostrar los siguientes mensajes: 
# a) Si el promedio es mayor a 35° mostrar el mensaje “Que semana tan calurosa” 
# b) Si el promedio esta entre 15° y 35° mostrar el mensaje “Que clima tan delicioso” 
# c) Si el promedio es menor de 15° mostrar el mensaje “Que semana tan fría”

suma = 0
temperatura = ([])

print('')
for x in range(7):   
    valores = int(input(f'Valor de la semana # {(x+1)}: '))
    temperatura.append(valores)

for i in temperatura:    
    suma = suma + i 
    promedio = suma / 7

if promedio >= 35:
    print(f'Total suma: {suma}')
    print('Que semana tan calurosa')
if promedio == 15 and promedio <= 34:
    print(f'Total suma: {suma}')
    print('Que clima tan delicioso')
if promedio < 15:
    print(f'Total suma: {suma}')
    print('Que semana tan fría')
else:
    print('Dato incorrecto')
