bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))

# Clasificación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
    
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))

# %s y % se utilizan para formatear cadenas de texto. Es una forma de insertar valores variables dentro de una cadena formateada

# %s se utiliza para indicar un marcador de posición en la cadena donde se insertará el valor de la variable nivel. El operador % se utiliza para combinar la cadena con la variable nivel. El valor de nivel se sustituirá en el marcador de posición %s.
