# update:inserta los valores de un conjunto a otro conjunto (o cualquier otro iterable)
# Si un elemento está presente en ambos conjuntos, sólo uno estará presente en el conjunto actualizado.
# set.update(set)

frutas = {"apple", "banana", "cherry"}
app = {"google", "microsoft", "apple"}

frutas.update(app)
print(frutas)  # {'apple', 'google', 'cherry', 'banana', 'microsoft'}
