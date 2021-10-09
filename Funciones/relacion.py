# Realiza una función llamada relación(a, b) que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

print('\nEl primer número es mayor que el segundo: {} '.format(relacion(5, 10)))  # -1
print('El primer número es menor que el segundo: {}'.format(relacion(10, 5)))  # 1
print('Los dos números son iguales: {}'.format(relacion(5, 5)))  # 0
