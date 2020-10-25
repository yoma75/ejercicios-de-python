# Dice cuantas veces se repiten los caracteres en cada cadena

contadores = {}

# 3 veces me pide el input
for i in range(3):
    cadena = input('Cadena de carácteres: ')
    for caracter in cadena:
        if caracter not in contadores.keys():
            #           clave 
            contadores[caracter] = 1
        else:
            contadores[caracter] += 1

# En vez de usar print,
for caracter, cantidad in contadores.items():
    print(caracter,':',cantidad)


