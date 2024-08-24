# Los OPERADORES LOGICOS se utilizan para combinar sentencias condicionales:

#  'and' retorna verdadero si ambas sentencias son verdaderas
x = 5
print(x > 3 and x < 10)  # True


# 'or' retorna verdadero si una de las sentencias es verdadera
x = 5
print(x > 3 or x < 4)  # True


# 'not' se utiliza para negar una expresión booleana
# El operador 'not' invierte el valor de la expresión: not True es False.
x = 5
print(not(x > 3 and x < 10))  # False
