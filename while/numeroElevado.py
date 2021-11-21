def run():
    LIMITE = 1000
    contador = 0

    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print(f'2 elevado a {contador} es igual a: {potencia_2}')
        contador = contador + 1
        potencia_2 = 2**contador

    # 2 elevado a 0 es igual a: 1
    # 2 elevado a 1 es igual a: 2
    # 2 elevado a 2 es igual a: 4
    # 2 elevado a 3 es igual a: 8
    # 2 elevado a 4 es igual a: 16
    # 2 elevado a 5 es igual a: 32
    # 2 elevado a 6 es igual a: 64
    # 2 elevado a 7 es igual a: 128
    # 2 elevado a 8 es igual a: 256
    # 2 elevado a 9 es igual a: 512

if __name__ == "__main__":
    run()
