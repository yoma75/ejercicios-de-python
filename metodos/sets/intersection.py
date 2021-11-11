# intersection: retorna un conjunto que contienen los items que existen entre dos o mas conjuntos

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)  # {'apple'}


# ---------------- ejemplo 2 ---------------
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)
print(result)  # {'c'}
