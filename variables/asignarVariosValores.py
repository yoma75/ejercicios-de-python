# Asignar valores a múltiples variables en una sola línea de codigo:
# El número de variables debe coincidir con el número de valores, o de lo contrario saldra un error.

x, y, z = "gato", "vaca", "elefante"
print(x)  # gato
print(y)  # vaca
print(z)  # elefante

# --------------------------------------------------------------------------------------------------------------

# Un valor para varias variables:
x = y = z = "Oso polar"
print(x)  # Oso polar
print(y)  # Oso polar
print(z)  # Oso polar

# --------------------------------------------------------------------------------------------------------------

# Si tiene una colección de valores en una lista, tupla, etc. Python le permite extraer los valores en variables. A esto se le llama desempaquetar (en ingles unpacking).

gatos = ["garfield", "silvestre", "cosmico"]
x, y, z = gatos
print(x)  # garfield
print(y)  # silvestre
print(z)  # cosmico
