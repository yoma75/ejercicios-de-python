# Repetir una cadena de caracteres

def producto_cadena(cadena, repeticion):
    resultado = ""

    for i in range(repeticion):
        resultado += cadena
    
    return resultado

print()
print(producto_cadena('Hola ', 3))
