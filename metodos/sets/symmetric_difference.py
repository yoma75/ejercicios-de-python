# symmetric_difference: retorna un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que estan presentes en ambos conjuntos.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)  # {'google', 'cherry', 'microsoft', 'banana'}

