# reversed: devuelve un objeto iterador invertido
# Invierte la secuencia de una lista

nuevo = []
letras = ['f','j','p', 'm', 'u']

invertidos = reversed(letras)

for x in invertidos:
    nuevo.append(x)

print(nuevo)  # ['u', 'm', 'p', 'j', 'f']
