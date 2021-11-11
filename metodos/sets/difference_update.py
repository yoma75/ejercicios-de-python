# difference_update: remueve los items que existen en ambos conjuntos

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)
print(x)  # {'cherry', 'banana'}

