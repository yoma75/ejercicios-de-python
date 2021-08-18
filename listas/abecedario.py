# Almacenar el abecedario en una lista, eliminar de la lista las letras que ocupen posiciones múltiplos de 3 y muestre por pantalla la lista resultante

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alphabet), 1, -1):
    if i % 3 == 0:
        alphabet.pop(i-1)
print(alphabet)

