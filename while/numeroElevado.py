def run():
    LIMITE = 1000
    contador = 0

    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print(f'2 elevado a {contador} es igual a: {potencia_2}')
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()
