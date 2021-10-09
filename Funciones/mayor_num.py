# Programa para determinar cuál es mayor entre 2 números cualquiera ingresados por el usuario

def mayor(a, b):
    if a > b:
        return print(f'El numero {a} es mayor que {b}')
    else:
        return print(f'El numero {a} es menor que {b}')
        
print('')
mayor(2,4)  # El numero 2 es menor que 4
mayor(45,19)  # El numero 45 es mayor que 19

