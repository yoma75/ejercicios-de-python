# --------- Metodos booleanos para strings -------------

cadena = 'Estoy mostrando los metodos booleanos para los strings'

# startswith: verifica si la cadena empieza con el parametro que le especifico.
print(cadena.startswith('E'))  # True
print(cadena.startswith('k'))  # False


# endswith: verifica si la cadena finaliza con el parametro que le especifico.
print(cadena.endswith('s'))  # True
print(cadena.endswith('m'))  # False


# isupper: verifica si la cadena esta toda en mayuscula
print(cadena.isupper())  # False


# islower: verifica si la cadena esta toda en minuscula
print(cadena.islower())  # False


# La mayoria de los valores son verdaderos
print(bool("abc"))  # True
print(bool(123))  # True
print(bool(["apple", "cherry", "banana"]))  # True


# Algunos valores son falsos:
print(bool(False))  # False
print(bool(None))  # False
print(bool(0))  # False
print(bool(""))  # False
print(bool(()))  # False
print(bool([]))  # False
print(bool({}))  # False


# Se puede ejecutar código basado en la respuesta booleana de una función:
# Imprima "YES!" si la función devuelve True, de lo contrario, imprima "¡NO!":
def myFuncion():
  return True

if myFuncion():
  print("Yes")  # Yes
else:
  print("No")
