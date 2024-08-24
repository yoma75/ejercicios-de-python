# Los OPERADORES DE PERTENENCIA se utilizan para verificar si un valor está presente dentro de una secuencia (como una lista, tupla, cadena de texto, conjunto o diccionario)

# 'in' devuelve True si el valor a la izquierda está presente en la secuencia a la derecha.
lista = [1, 2, 3, 4, 5]
print(3 in lista)  # True, porque 3 está en la lista

cadena = "hello"
print('e' in cadena)  # True, porque 'e' está en la cadena

# -------------------------------------------------------------------------------------------------------------

# 'not in': devuelve True si el valor a la izquierda no está presente en la secuencia a la derecha.
lista = [1, 2, 3, 4, 5]
print(6 not in lista)  # True, porque 6 no está en la lista

cadena = "hello"
print('x' not in cadena)  # True, porque 'x' no está en la cadena
