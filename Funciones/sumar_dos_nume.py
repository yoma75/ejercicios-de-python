# Sumar Dos Números. Si la Suma se Halla entre 10 y 30, Retornar 30


def sumar(x, y):
    suma = x + y

    if suma in range(10, 31):
        return 30
    else:
        return suma

print(sumar(12, 23))
print(sumar(2, 3))
print(sumar(11, 17))