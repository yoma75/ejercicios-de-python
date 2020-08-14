# Tabla de multiplicar

def run():
    numero = int(input('Numero de la tabla que desea saber: '.upper()))

    for x in range(1,11):
        print(f'{numero} x {x} : {numero*x}')


if __name__ == "__main__":
    run()
