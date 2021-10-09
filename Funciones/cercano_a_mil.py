# Crear una Función para Determinar si un Número es Cercano a 1000

def cercania(n):
    # abs: valor absoluto
    # que no se separe a < 100 unidades

    # Comprueba si un numero es cercano a 1000 o a 2000
    return (abs(1000-n) < 100) or (abs(2000 - n) < 100)

print(cercania(1000))  # True
print(cercania(950))  # True
print(cercania(200))  #False
