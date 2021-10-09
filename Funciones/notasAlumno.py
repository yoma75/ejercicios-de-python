def noticas(puntuacion):
    if puntuacion > 0.9 and puntuacion <= 0.99:
        return print('Sobresaliente')
    elif puntuacion > 0.8:
        return print('notable')
    elif puntuacion > 0.7:
        return print('bien')
    elif puntuacion > 0.6:
        return print('suficiente')
    elif puntuacion <= 0.6:
        return print('insuficiente')
    else:
        return print('La nota no sirve')

noticas(0.96)  # Sobresaliente
noticas(0.34)  # insuficiente
