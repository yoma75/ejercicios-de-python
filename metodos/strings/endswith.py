# endswith(): Compruebe si la cadena termina con el signo de puntuación asignado

texto = 'Hola, bienvenido a Python!'

print(texto.endswith('!'))  # True
print(texto.endswith('.'))  # False


# Cpmprueba si la cadena de texto termina en Python!
print(texto.endswith('Python!'))  # True


# Verifique si en la posición 0 a la 5 termina con la palabra "Hola":
print(texto.endswith('Hola', 0, 4))  # True
