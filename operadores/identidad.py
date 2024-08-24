# Los OPERADORES DE IDENTIDAD se utilizan para comparar la identidad de dos objetos, es decir, para verificar si dos referencias de objeto apuntan al mismo lugar en la memoria.

# 'is': verifica si ambas variables apuntan al mismo lugar en la memoria.
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, porque a y b son el mismo objeto
print(a is c)  # False, porque a y c son objetos diferentes aunque tengan el mismo contenido

# -------------------------------------------------------------------------------------------------------------

# 'is not': devuelve True si los dos objetos que se están comparando no son el mismo objeto en la memoria.
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is not b)  # False, porque a y b son el mismo objeto
print(a is not c)  # True, porque a y c son objetos diferentes
