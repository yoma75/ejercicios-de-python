# Sumar Tres Números Si Todos Son Diferentes, en Caso Devolver 0

def sumar(x, y, z):
    if x == y or x == z or y == z:
        return 0
    else:
        return x+y+z


print(sumar(2,3,5))
print(sumar(2,5,2))
print(sumar(5,5,2))
print(sumar(11,7,5))


