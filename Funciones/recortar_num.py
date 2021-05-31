# Realiza una función llamada recortar(numero, mínimo, maximo) que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10.

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero

print('\nEl número recortado es: {}'.format(recortar(15, 0, 10)))   # 10
print('El número recortado es: {}'.format(recortar(34, 3, 6)))      # 6
print('El número recortado es: {}'.format(recortar(56, 12, 30)))    # 30
print('El número recortado es: {}'.format(recortar(5, 20, 65)))     # 20




