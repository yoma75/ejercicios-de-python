# Calcular la Diferencia de Conjuntos con Elementos con Nombres de Colores

colores_lista1 = ['Negro', 'Rojo', 'Verde', 'Blanco']
colores_lista2 = ['Blanco', 'Azul', 'Verde', 'Gris', 'Amarillo', 'Verde']

conjunto1 = set(colores_lista1)
conjunto2 = set(colores_lista2)

print()

# Muestra los colores del conjunto1 que no están presentes en el conjunto2
diferencia = conjunto1.difference(conjunto2)
print(diferencia) # {'Negro', 'Rojo'}


