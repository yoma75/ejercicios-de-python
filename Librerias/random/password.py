import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        # choise: escoje al azar un caracter de cada una de las listas creadas por mi
        caracter_random = random.choice(caracteres) 
        contrasena.append(caracter_random)

    # Convertir una lista en un string
    # '' representa un string vacio
    # join: string unidos en una sola cadena
    contrasena = "".join(contrasena)
    return contrasena # return: para que se guarde en contrasena


def run():
    contrasena = generar_contrasena()
    print('\nTu nueva contraseña es: '.upper() + contrasena)


if __name__ == '__main__':
    run()