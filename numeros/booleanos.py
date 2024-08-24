# Pide al usuario dos números enteros, y da el valor True a una variable booleana llamada "ambosPares" en caso de que los dos sean pares, o el valor False en caso contrario. 

n1 = int(input('Digite un número: '))
n2 = int(input('Digite otro número: '))

ambosPares = ((n1 % 2 == 0) and (n2 % 2 == 0))
print(f'Los dos números son pares?.... {ambosPares}')  # Los dos números son pares? True
