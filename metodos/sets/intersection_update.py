# intersection_update: remueve los items que estan presentes en ambos conjuntos

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)  # {'apple'}

